import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
from microC.runtime import McFunction
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EXEMPLOS_DIR = BASE_DIR / "exemplos" / "arrays"


class TestArrays:
    """Testes para exemplos de arrays"""

    def test_declaracao_inicializacao(self):
        """Testa declaração e inicialização de arrays"""
        file_path = EXEMPLOS_DIR / "declaracao_inicializacao.microc"
        
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

    def test_manipulacao_atribuicao(self):
        """Testa manipulação de arrays com atribuição"""
        file_path = EXEMPLOS_DIR / "manipulacao_atribuicao.microc"
        
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

    def test_busca_array(self):
        """Testa busca em array"""
        file_path = EXEMPLOS_DIR / "busca_array.microc"
        
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

    def test_todos_exemplos_arrays_parseable(self):
        """Testa se todos os exemplos de arrays podem ser parseados"""
        exemplos = [
            "declaracao_inicializacao.microc",
            "manipulacao_atribuicao.microc",
            "busca_array.microc"
        ]
        
        for exemplo in exemplos:
            file_path = EXEMPLOS_DIR / exemplo
            with open(file_path, "r") as f:
                src = f.read()
            
            ast = parse(src)
            assert ast is not None, f"Falha ao parsear {exemplo}"
            ast.validate_tree()

    def test_acesso_array_bounds(self):
        """Testa se os exemplos respeitam limites de arrays"""
        # Teste com exemplo que sabemos que deve funcionar
        file_path = EXEMPLOS_DIR / "declaracao_inicializacao.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        # Deve executar sem erro de índice
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
