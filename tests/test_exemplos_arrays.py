import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
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
        
        # Verifica se os arrays foram criados
        assert 'numeros' in ctx
        assert 'letras' in ctx
        
        # Verifica conteúdo dos arrays
        numeros = ctx['numeros']
        letras = ctx['letras']
        
        assert isinstance(numeros, list)
        assert isinstance(letras, list)
        assert len(numeros) == 5
        assert len(letras) == 3
        assert numeros[0] == 1
        assert numeros[4] == 5
        assert letras[1] == 'B'

    def test_manipulacao_atribuicao(self):
        """Testa manipulação de arrays com atribuição"""
        file_path = EXEMPLOS_DIR / "manipulacao_atribuicao.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se o array foi criado e preenchido
        assert 'dados' in ctx
        dados = ctx['dados']
        
        assert isinstance(dados, list)
        assert len(dados) == 4
        assert dados[0] == 10
        assert dados[1] == 20
        assert dados[2] == 30
        assert dados[3] == 40

    def test_busca_array(self):
        """Testa busca em array"""
        file_path = EXEMPLOS_DIR / "busca_array.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a busca encontrou o elemento
        assert 'valores' in ctx
        assert 'procurado' in ctx
        assert 'encontrado' in ctx
        assert 'posicao' in ctx
        
        valores = ctx['valores']
        assert isinstance(valores, list)
        assert 42 in valores
        assert ctx['procurado'] == 42
        assert ctx['encontrado'] == 1  # True
        assert ctx['posicao'] == 3  # Posição do 42 no array

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
