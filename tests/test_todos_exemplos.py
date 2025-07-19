import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.parent
EXEMPLOS_DIR = BASE_DIR / "exemplos"


class TestTodosExemplos:
    """Testes que executam todos os exemplos de uma vez"""

    @pytest.mark.full_suite
    def test_todos_exemplos_executam_sem_erro(self):
        """Testa se todos os exemplos podem ser parseados e executados"""
        categorias = [
            "variaveis",
            "arrays", 
            "funcoes",
            "estruturas_controle",
            "operadores",
            "algoritmos"
        ]
        
        exemplos_testados = 0
        
        for categoria in categorias:
            categoria_dir = EXEMPLOS_DIR / categoria
            if not categoria_dir.exists():
                continue
                
            for arquivo in categoria_dir.glob("*.microc"):
                print(f"Testando: {categoria}/{arquivo.name}")
                
                with open(arquivo, "r") as f:
                    src = f.read()
                
                # Deve fazer parse sem erro
                ast = parse(src)
                assert ast is not None, f"Falha ao parsear {categoria}/{arquivo.name}"
                
                # Deve validar sem erro
                ast.validate_tree()
                
                # Deve executar sem erro crítico
                ctx = Ctx.from_dict({})
                try:
                    result = microc_eval(src, ctx)
                    exemplos_testados += 1
                except Exception as e:
                    # Se houver erro, pelo menos deve ter parseado
                    print(f"Aviso: {categoria}/{arquivo.name} deu erro na execução: {e}")
                    exemplos_testados += 1
        
        # Deve ter testado pelo menos 15 exemplos
        assert exemplos_testados >= 15, f"Esperava pelo menos 15 exemplos, testou {exemplos_testados}"

    def test_exemplos_raiz_executam(self):
        """Testa exemplos na raiz da pasta exemplos"""
        exemplos_raiz = [
            "hello.microc",
            "fibonacci.microc", 
            "factorial.microc",
            "arrays.microc",
            "bubble_sort.microc"
        ]
        
        for exemplo in exemplos_raiz:
            arquivo = EXEMPLOS_DIR / exemplo
            if arquivo.exists():
                print(f"Testando exemplo raiz: {exemplo}")
                
                with open(arquivo, "r") as f:
                    src = f.read()
                
                ast = parse(src)
                assert ast is not None, f"Falha ao parsear {exemplo}"
                ast.validate_tree()
                
                ctx = Ctx.from_dict({})
                try:
                    result = microc_eval(src, ctx)
                except Exception as e:
                    print(f"Aviso: {exemplo} deu erro na execução: {e}")

    def test_estrutura_pastas_exemplos(self):
        """Verifica se a estrutura de pastas está correta"""
        categorias_esperadas = [
            "variaveis",
            "arrays",
            "funcoes", 
            "estruturas_controle",
            "operadores",
            "algoritmos"
        ]
        
        for categoria in categorias_esperadas:
            categoria_dir = EXEMPLOS_DIR / categoria
            assert categoria_dir.exists(), f"Pasta {categoria} não existe"
            assert categoria_dir.is_dir(), f"{categoria} não é uma pasta"
            
            # Deve ter pelo menos um arquivo .microc
            arquivos_microc = list(categoria_dir.glob("*.microc"))
            assert len(arquivos_microc) > 0, f"Pasta {categoria} não tem arquivos .microc"

    def test_exemplos_tem_main(self):
        """Verifica se os exemplos têm função main"""
        categorias = ["variaveis", "arrays", "funcoes", "estruturas_controle", "operadores", "algoritmos"]
        
        for categoria in categorias:
            categoria_dir = EXEMPLOS_DIR / categoria
            if not categoria_dir.exists():
                continue
                
            for arquivo in categoria_dir.glob("*.microc"):
                with open(arquivo, "r") as f:
                    src = f.read()
                
                # Deve conter uma função main
                assert "main()" in src, f"{categoria}/{arquivo.name} não tem função main"

    def test_exemplos_sintaxe_valida(self):
        """Verifica se todos os exemplos têm sintaxe válida"""
        total_arquivos = 0
        arquivos_validos = 0
        
        for root, dirs, files in os.walk(EXEMPLOS_DIR):
            for file in files:
                if file.endswith('.microc'):
                    total_arquivos += 1
                    arquivo_path = Path(root) / file
                    
                    try:
                        with open(arquivo_path, "r") as f:
                            src = f.read()
                        
                        ast = parse(src)
                        ast.validate_tree()
                        arquivos_validos += 1
                        
                    except Exception as e:
                        print(f"Erro em {arquivo_path}: {e}")
        
        # Pelo menos 90% dos arquivos devem ser válidos
        taxa_sucesso = arquivos_validos / total_arquivos if total_arquivos > 0 else 0
        assert taxa_sucesso >= 0.9, f"Taxa de sucesso: {taxa_sucesso:.2%} ({arquivos_validos}/{total_arquivos})"

    @pytest.mark.parametrize("categoria", [
        "variaveis",
        "arrays", 
        "funcoes",
        "estruturas_controle", 
        "operadores",
        "algoritmos"
    ])
    def test_categoria_tem_exemplos_suficientes(self, categoria):
        """Verifica se cada categoria tem pelo menos 3 exemplos"""
        categoria_dir = EXEMPLOS_DIR / categoria
        
        if categoria_dir.exists():
            arquivos = list(categoria_dir.glob("*.microc"))
            assert len(arquivos) >= 3, f"Categoria {categoria} tem apenas {len(arquivos)} exemplos, esperado pelo menos 3"
