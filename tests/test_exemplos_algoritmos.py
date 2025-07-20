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
        
        # Verifica se as funções foram definidas
        assert 'selectionSort' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        selection_sort_tuple = ctx.scope['selectionSort']
        main_tuple = ctx.scope['main']
        
        assert isinstance(selection_sort_tuple[1], McFunction)
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        # Para verificar se funcionam, precisaríamos chamar main()
        main_func = main_tuple[1]
        selection_sort_func = selection_sort_tuple[1]
        
        assert main_func.name == 'main'
        assert main_func.type == 'int'
        assert selection_sort_func.name == 'selectionSort'
        assert selection_sort_func.type == 'void'

    def test_busca_binaria(self):
        """Testa busca binária em array ordenado"""
        file_path = EXEMPLOS_DIR / "busca_binaria.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as funções foram definidas
        assert 'buscaBinaria' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        busca_binaria_tuple = ctx.scope['buscaBinaria']
        main_tuple = ctx.scope['main']
        
        assert isinstance(busca_binaria_tuple[1], McFunction)
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        busca_binaria_func = busca_binaria_tuple[1]
        
        assert main_func.name == 'main'
        assert main_func.type == 'int'
        assert busca_binaria_func.name == 'buscaBinaria'
        assert busca_binaria_func.type == 'int'

    def test_kadane_algorithm(self):
        """Testa algoritmo de Kadane para maior subsequência contígua"""
        file_path = EXEMPLOS_DIR / "kadane_algorithm.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se as funções foram definidas
        assert 'maxSubarraySum' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        max_subarray_tuple = ctx.scope['maxSubarraySum']
        main_tuple = ctx.scope['main']
        
        assert isinstance(max_subarray_tuple[1], McFunction)
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        max_subarray_func = max_subarray_tuple[1]
        
        assert main_func.name == 'main'
        assert main_func.type == 'int'
        assert max_subarray_func.name == 'maxSubarraySum'
        assert max_subarray_func.type == 'int'

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
        
        # Verifica se as funções foram definidas
        assert 'fibonacciIterativo' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        fib_tuple = ctx.scope['fibonacciIterativo']
        main_tuple = ctx.scope['main']
        
        assert isinstance(fib_tuple[1], McFunction)
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        fib_func = fib_tuple[1]
        
        assert main_func.name == 'main'
        assert main_func.type == 'int'
        assert fib_func.name == 'fibonacciIterativo'
        assert fib_func.type == 'int'

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
        
        # Verifica se as funções foram definidas
        assert 'fatorialIterativo' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        fat_tuple = ctx.scope['fatorialIterativo']
        main_tuple = ctx.scope['main']
        
        assert isinstance(fat_tuple[1], McFunction)
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        fat_func = fat_tuple[1]
        
        assert main_func.name == 'main'
        assert main_func.type == 'int'
        assert fat_func.name == 'fatorialIterativo'
        assert fat_func.type == 'int'

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
        
        # Verifica se as funções foram definidas
        assert 'buscaLinear' in ctx
        assert 'main' in ctx
        
        # ctx stores variables as (Type, value) tuples
        busca_tuple = ctx.scope['buscaLinear']
        main_tuple = ctx.scope['main']
        
        assert isinstance(busca_tuple[1], McFunction)
        assert isinstance(main_tuple[1], McFunction)
        
        # O código só define as funções, não as executa
        main_func = main_tuple[1]
        busca_func = busca_tuple[1]
        
        assert main_func.name == 'main'
        assert main_func.type == 'int'
        assert busca_func.name == 'buscaLinear'
        assert busca_func.type == 'int'
