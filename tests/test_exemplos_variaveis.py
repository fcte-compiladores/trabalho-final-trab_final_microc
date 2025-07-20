import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
from microC.runtime import McFunction
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EXEMPLOS_DIR = BASE_DIR / "exemplos" / "variaveis"


class TestVariaveis:
    """Testes para exemplos de variáveis"""

    def test_declaracao_basica(self):
        """Testa declaração e inicialização básica de variáveis"""
        file_path = EXEMPLOS_DIR / "declaracao_basica.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        # Deve fazer parse sem erro
        ast = parse(src)
        assert ast is not None
        
        # Deve executar sem erro
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

    def test_atribuicao_posterior(self):
        """Testa variáveis sem inicialização e atribuição posterior"""
        file_path = EXEMPLOS_DIR / "atribuicao_posterior.microc"
        
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

    def test_escopo_blocos(self):
        """Testa escopo de variáveis em blocos"""
        file_path = EXEMPLOS_DIR / "escopo_blocos.microc"
        
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

    def test_todos_exemplos_variaveis_parseable(self):
        """Testa se todos os exemplos de variáveis podem ser parseados"""
        exemplos = [
            "declaracao_basica.microc",
            "atribuicao_posterior.microc", 
            "escopo_blocos.microc"
        ]
        
        for exemplo in exemplos:
            file_path = EXEMPLOS_DIR / exemplo
            with open(file_path, "r") as f:
                src = f.read()
            
            # Deve fazer parse sem erro
            ast = parse(src)
            assert ast is not None, f"Falha ao parsear {exemplo}"
            
            # Deve validar sem erro
            ast.validate_tree()
