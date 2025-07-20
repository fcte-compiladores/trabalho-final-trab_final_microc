import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
from microC.runtime import McFunction
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EXEMPLOS_DIR = BASE_DIR / "exemplos" / "estruturas_controle"


class TestEstruturasControle:
    """Testes para exemplos de estruturas de controle"""

    def test_condicionais(self):
        """Testa estruturas condicionais if/else"""
        file_path = EXEMPLOS_DIR / "condicionais.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função main foi definida
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        assert main_func.name == 'main'
        assert main_func.type == 'int'

    def test_lacos_while(self):
        """Testa laços while e do-while"""
        file_path = EXEMPLOS_DIR / "lacos_while.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função main foi definida
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        assert main_func.name == 'main'
        assert main_func.type == 'int'

    def test_lacos_for(self):
        """Testa diferentes variações do laço for"""
        file_path = EXEMPLOS_DIR / "lacos_for.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função main foi definida
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        assert main_func.name == 'main'
        assert main_func.type == 'int'

    def test_todos_exemplos_estruturas_parseable(self):
        """Testa se todos os exemplos de estruturas podem ser parseados"""
        exemplos = [
            "condicionais.microc",
            "lacos_while.microc",
            "lacos_for.microc"
        ]
        
        for exemplo in exemplos:
            file_path = EXEMPLOS_DIR / exemplo
            with open(file_path, "r") as f:
                src = f.read()
            
            ast = parse(src)
            assert ast is not None, f"Falha ao parsear {exemplo}"
            ast.validate_tree()

    def test_if_else_aninhado(self):
        """Testa estruturas if/else aninhadas"""
        src = """
        int main() {
            int x = 15;
            int resultado = 0;
            
            if (x > 10) {
                if (x > 20) {
                    resultado = 3;
                } else {
                    resultado = 2;
                }
            } else {
                resultado = 1;
            }
            
            return 0;
        }
        """
        
        ast = parse(src)
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função main foi definida
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        assert main_func.name == 'main'
        assert main_func.type == 'int'

    def test_while_aninhado(self):
        """Testa laços while aninhados"""
        src = """
        int main() {
            int i = 0;
            int j = 0;
            int soma = 0;
            
            while (i < 3) {
                j = 0;
                while (j < 2) {
                    soma++;
                    j++;
                }
                i++;
            }
            
            return 0;
        }
        """
        
        ast = parse(src)
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função main foi definida
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        assert main_func.name == 'main'
        assert main_func.type == 'int'

    def test_for_com_break_simulado(self):
        """Testa simulação de break em for usando variável de controle"""
        src = """
        int main() {
            int encontrado = 0;
            int valor = 0;
            
            for (int i = 0; i < 10 && !encontrado; i++) {
                if (i == 5) {
                    encontrado = 1;
                    valor = i;
                }
            }
            
            return 0;
        }
        """
        
        ast = parse(src)
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função main foi definida
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        main_tuple = ctx.scope['main']
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        assert main_func.name == 'main'
        assert main_func.type == 'int'
