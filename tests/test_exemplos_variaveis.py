import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
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
        
        # Verifica se as variáveis foram declaradas corretamente
        assert 'x' in ctx
        assert 'y' in ctx
        assert 'c' in ctx
        assert ctx['x'] == 10
        assert ctx['y'] == 20
        assert ctx['c'] == 'A'

    def test_atribuicao_posterior(self):
        """Testa variáveis sem inicialização e atribuição posterior"""
        file_path = EXEMPLOS_DIR / "atribuicao_posterior.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as atribuições funcionaram
        assert 'a' in ctx
        assert 'letra' in ctx
        assert ctx['a'] == 42
        assert ctx['letra'] == 'Z'

    def test_escopo_blocos(self):
        """Testa escopo de variáveis em blocos"""
        file_path = EXEMPLOS_DIR / "escopo_blocos.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Variável global deve existir
        assert 'global_var' in ctx
        assert ctx['global_var'] == 100
        
        # Variável local não deve existir no escopo global
        assert 'local_var' not in ctx

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
