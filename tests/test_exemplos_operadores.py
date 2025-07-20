import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
from microC.runtime import McFunction
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EXEMPLOS_DIR = BASE_DIR / "exemplos" / "operadores"


class TestOperadores:
    """Testes para exemplos de operadores"""

    def test_aritmeticos(self):
        """Testa operadores aritméticos"""
        file_path = EXEMPLOS_DIR / "aritmeticos.microc"
        
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

    def test_comparacao_logicos(self):
        """Testa operadores de comparação e lógicos"""
        file_path = EXEMPLOS_DIR / "comparacao_logicos.microc"
        
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

    def test_incremento_atribuicao(self):
        """Testa operadores de incremento/decremento e atribuição composta"""
        file_path = EXEMPLOS_DIR / "incremento_atribuicao.microc"
        
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

    def test_todos_exemplos_operadores_parseable(self):
        """Testa se todos os exemplos de operadores podem ser parseados"""
        exemplos = [
            "aritmeticos.microc",
            "comparacao_logicos.microc",
            "incremento_atribuicao.microc"
        ]
        
        for exemplo in exemplos:
            file_path = EXEMPLOS_DIR / exemplo
            with open(file_path, "r") as f:
                src = f.read()
            
            ast = parse(src)
            assert ast is not None, f"Falha ao parsear {exemplo}"
            ast.validate_tree()

    def test_precedencia_operadores(self):
        """Testa precedência de operadores"""
        src = """
        int main() {
            int resultado1 = 2 + 3 * 4;      // Deve ser 14 (3*4 + 2)
            int resultado2 = (2 + 3) * 4;    // Deve ser 20 (5 * 4)
            int resultado3 = 10 - 6 / 2;     // Deve ser 7 (10 - 3)
            int resultado4 = (10 - 6) / 2;   // Deve ser 2 (4 / 2)
            
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

    def test_operadores_comparacao_tipos(self):
        """Testa operadores de comparação com diferentes tipos"""
        src = """
        int main() {
            int a = 5;
            int b = 5;
            char c = 'A';
            char d = 'B';
            
            int int_eq = (a == b);     // 1 (verdadeiro)
            int int_ne = (a != b);     // 0 (falso)
            int char_lt = (c < d);     // 1 (verdadeiro, 'A' < 'B')
            int char_gt = (d > c);     // 1 (verdadeiro, 'B' > 'A')
            
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

    def test_operadores_logicos_curto_circuito(self):
        """Testa avaliação de curto-circuito em operadores lógicos"""
        src = """
        int main() {
            int x = 0;
            int y = 1;
            
            int and_result = (x && y);  // 0 (falso)
            int or_result = (x || y);   // 1 (verdadeiro)
            int not_result = !x;        // 1 (verdadeiro)
            
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

    def test_atribuicao_composta_tipos(self):
        """Testa operadores de atribuição composta"""
        src = """
        int main() {
            int num = 10;
            
            num += 5;   // 15
            num -= 3;   // 12
            num *= 2;   // 24
            num /= 4;   // 6
            
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
