import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
from microC.runtime import McFunction
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
EXEMPLOS_DIR = BASE_DIR / "exemplos" / "algoritmos"


class TestAlgoritmos:
    """Testes para exemplos de algoritmos"""

    def test_selection_sort(self):
        """Testa algoritmo de ordenação Selection Sort"""
        file_path = EXEMPLOS_DIR / "selection_sort.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função foi definida
        assert 'selectionSort' in ctx
        assert isinstance(ctx['selectionSort'], McFunction)
        
        # Verifica se o array foi ordenado
        assert 'dados' in ctx
        assert 'tamanho' in ctx
        
        dados = ctx['dados']
        assert isinstance(dados, list)
        assert len(dados) == 6
        
        # Verifica se está ordenado
        for i in range(len(dados) - 1):
            assert dados[i] <= dados[i + 1], f"Array não está ordenado: {dados}"

    def test_busca_binaria(self):
        """Testa busca binária em array ordenado"""
        file_path = EXEMPLOS_DIR / "busca_binaria.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função foi definida
        assert 'buscaBinaria' in ctx
        assert isinstance(ctx['buscaBinaria'], McFunction)
        
        # Verifica variáveis
        assert 'numeros' in ctx
        assert 'procurado' in ctx
        assert 'resultado' in ctx
        
        numeros = ctx['numeros']
        assert isinstance(numeros, list)
        # Array deve estar ordenado: [2, 5, 8, 12, 16, 23, 38, 45]
        assert numeros == [2, 5, 8, 12, 16, 23, 38, 45]

    def test_kadane_algorithm(self):
        """Testa algoritmo de Kadane para maior subsequência contígua"""
        file_path = EXEMPLOS_DIR / "kadane_algorithm.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se a função foi definida
        assert 'maxSubarraySum' in ctx
        assert isinstance(ctx['maxSubarraySum'], McFunction)
        
        # Verifica variáveis
        assert 'numeros' in ctx
        assert 'resultado' in ctx
        
        numeros = ctx['numeros']
        resultado = ctx['resultado']
        
        assert isinstance(numeros, list)
        # Para o array [-2, 1, -3, 4, -1, 2, 1, -5], a maior soma é 6
        assert resultado == 6

    def test_todos_exemplos_algoritmos_parseable(self):
        """Testa se todos os exemplos de algoritmos podem ser parseados"""
        exemplos = [
            "selection_sort.microc",
            "busca_binaria.microc",
            "kadane_algorithm.microc"
        ]
        
        for exemplo in exemplos:
            file_path = EXEMPLOS_DIR / exemplo
            with open(file_path, "r") as f:
                src = f.read()
            
            ast = parse(src)
            assert ast is not None, f"Falha ao parsear {exemplo}"
            ast.validate_tree()

    def test_ordenacao_bubble_sort(self):
        """Testa bubble sort (se existir o arquivo)"""
        bubble_sort_path = BASE_DIR / "exemplos" / "bubble_sort.microc"
        
        if bubble_sort_path.exists():
            with open(bubble_sort_path, "r") as f:
                src = f.read()
            
            ast = parse(src)
            assert ast is not None
            
            ctx = Ctx.from_dict({})
            result = microc_eval(src, ctx)
            
            # Verifica se o array foi ordenado
            assert 'arr' in ctx
            arr = ctx['arr']
            assert isinstance(arr, list)
            
            # Verifica se está ordenado
            for i in range(len(arr) - 1):
                assert arr[i] <= arr[i + 1]

    def test_algoritmo_fibonacci_iterativo(self):
        """Testa implementação iterativa de Fibonacci"""
        src = """
        int fibonacciIterativo(int n) {
            if (n <= 1) {
                return n;
            }
            
            int a = 0;
            int b = 1;
            int temp = 0;
            
            for (int i = 2; i <= n; i++) {
                temp = a + b;
                a = b;
                b = temp;
            }
            
            return b;
        }
        
        int main() {
            int resultado = fibonacciIterativo(10);
            return 0;
        }
        """
        
        ast = parse(src)
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        assert 'fibonacciIterativo' in ctx
        assert 'resultado' in ctx
        # F(10) = 55
        assert ctx['resultado'] == 55

    def test_algoritmo_fatorial_iterativo(self):
        """Testa implementação iterativa de fatorial"""
        src = """
        int fatorialIterativo(int n) {
            int resultado = 1;
            for (int i = 1; i <= n; i++) {
                resultado *= i;
            }
            return resultado;
        }
        
        int main() {
            int fat5 = fatorialIterativo(5);
            return 0;
        }
        """
        
        ast = parse(src)
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        assert 'fatorialIterativo' in ctx
        assert 'fat5' in ctx
        # 5! = 120
        assert ctx['fat5'] == 120

    def test_busca_linear(self):
        """Testa algoritmo de busca linear"""
        src = """
        int buscaLinear(int arr[], int n, int procurado) {
            for (int i = 0; i < n; i++) {
                if (arr[i] == procurado) {
                    return i;
                }
            }
            return -1;
        }
        
        int main() {
            int dados[5] = {10, 20, 30, 40, 50};
            int posicao = buscaLinear(dados, 5, 30);
            return 0;
        }
        """
        
        ast = parse(src)
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        assert 'buscaLinear' in ctx
        assert 'dados' in ctx
        assert 'posicao' in ctx
        # 30 está na posição 2
        assert ctx['posicao'] == 2
