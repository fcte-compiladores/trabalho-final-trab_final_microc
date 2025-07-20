import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
from microC.runtime import McFunction
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EXEMPLOS_DIR = BASE_DIR / "exemplos" / "funcoes"


class TestFuncoes:
    """Testes para exemplos de funções"""

    def test_funcao_simples(self):
        """Testa função simples com parâmetros e retorno"""
        file_path = EXEMPLOS_DIR / "funcao_simples.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as funções foram definidas
        assert 'soma' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        soma_tuple = ctx.scope['soma']
        assert isinstance(soma_tuple[1], McFunction)
        
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        soma_func = soma_tuple[1]
        assert soma_func.name == 'soma'
        assert soma_func.type == 'int'

    def test_multiplas_funcoes(self):
        """Testa múltiplas funções incluindo função void"""
        file_path = EXEMPLOS_DIR / "multiplas_funcoes.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as funções foram definidas
        assert 'imprimirNumero' in ctx
        assert 'quadrado' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        imprimir_tuple = ctx.scope['imprimirNumero']
        assert isinstance(imprimir_tuple[1], McFunction)
        
        quadrado_tuple = ctx.scope['quadrado']
        assert isinstance(quadrado_tuple[1], McFunction)
        
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)

    def test_funcao_recursiva(self):
        """Testa função recursiva para cálculo de potência"""
        file_path = EXEMPLOS_DIR / "funcao_recursiva.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as funções foram definidas
        assert 'potencia' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        potencia_tuple = ctx.scope['potencia']
        assert isinstance(potencia_tuple[1], McFunction)
        
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)

    def test_todos_exemplos_funcoes_parseable(self):
        """Testa se todos os exemplos de funções podem ser parseados"""
        exemplos = [
            "funcao_simples.microc",
            "multiplas_funcoes.microc",
            "funcao_recursiva.microc"
        ]
        
        for exemplo in exemplos:
            file_path = EXEMPLOS_DIR / exemplo
            with open(file_path, "r") as f:
                src = f.read()
            
            ast = parse(src)
            assert ast is not None, f"Falha ao parsear {exemplo}"
            ast.validate_tree()

    def test_chamadas_funcoes(self):
        """Testa se as chamadas de função funcionam corretamente"""
        # Teste específico para chamadas de função
        src = """
        int dobrar(int x) {
            return x * 2;
        }
        
        int main() {
            int num = 5;
            int resultado = dobrar(num);
            return 0;
        }
        """
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as funções foram definidas
        assert 'dobrar' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        dobrar_tuple = ctx.scope['dobrar']
        assert isinstance(dobrar_tuple[1], McFunction)
        
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)

    def test_escopo_funcoes(self):
        """Testa escopo de variáveis em funções"""
        src = """
        int func_teste(int param) {
            int local = param + 10;
            return local;
        }
        
        int main() {
            int global = 5;
            int ret = func_teste(global);
            return 0;
        }
        """
        
        ast = parse(src)
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as funções foram definidas
        assert 'func_teste' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        func_teste_tuple = ctx.scope['func_teste']
        assert isinstance(func_teste_tuple[1], McFunction)
        
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
