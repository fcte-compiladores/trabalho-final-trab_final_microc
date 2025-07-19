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
        
        # Verifica se a função foi definida
        assert 'soma' in ctx
        assert isinstance(ctx['soma'], McFunction)
        
        # Verifica se o resultado da chamada está correto
        assert 'resultado' in ctx
        assert ctx['resultado'] == 40  # soma(15, 25)

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
        assert isinstance(ctx['imprimirNumero'], McFunction)
        assert isinstance(ctx['quadrado'], McFunction)
        
        # Verifica variáveis do main
        assert 'valor' in ctx
        assert 'quad' in ctx
        assert ctx['valor'] == 7
        assert ctx['quad'] == 49  # 7^2

    def test_funcao_recursiva(self):
        """Testa função recursiva para cálculo de potência"""
        file_path = EXEMPLOS_DIR / "funcao_recursiva.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função foi definida
        assert 'potencia' in ctx
        assert isinstance(ctx['potencia'], McFunction)
        
        # Verifica os resultados
        assert 'resultado1' in ctx
        assert 'resultado2' in ctx
        assert ctx['resultado1'] == 8   # 2^3
        assert ctx['resultado2'] == 25  # 5^2

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
        
        assert 'dobrar' in ctx
        assert 'num' in ctx
        assert 'resultado' in ctx
        assert ctx['num'] == 5
        assert ctx['resultado'] == 10

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
        
        # Variáveis locais da função não devem existir no escopo global
        assert 'param' not in ctx
        assert 'local' not in ctx
        # Variáveis do main devem existir
        assert 'global' in ctx
        assert 'ret' in ctx
        assert ctx['ret'] == 15
