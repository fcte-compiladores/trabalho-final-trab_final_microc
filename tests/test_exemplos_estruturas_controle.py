import pytest
from microC import parse, eval as microc_eval
from microC.ctx import Ctx
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
        
        # Verifica se as variáveis foram criadas
        assert 'idade' in ctx
        assert 'nota' in ctx
        assert ctx['idade'] == 18
        assert ctx['nota'] == 85

    def test_lacos_while(self):
        """Testa laços while e do-while"""
        file_path = EXEMPLOS_DIR / "lacos_while.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica estado final das variáveis
        assert 'contador' in ctx
        assert 'num' in ctx
        # Contador deve ter parado em 6 (while contador <= 5)
        assert ctx['contador'] == 6
        # Num deve ter parado em 7 (do-while num > 7)
        assert ctx['num'] == 7

    def test_lacos_for(self):
        """Testa diferentes variações do laço for"""
        file_path = EXEMPLOS_DIR / "lacos_for.microc"
        
        with open(file_path, "r") as f:
            src = f.read()
        
        ast = parse(src)
        assert ast is not None
        
        ctx = Ctx.from_dict({})
        result = microc_eval(src, ctx)
        
        # Verifica se os laços executaram (variáveis devem existir)
        assert 'i' in ctx
        assert 'j' in ctx
        assert 'linha' in ctx
        assert 'col' in ctx

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
        
        assert ctx['x'] == 15
        assert ctx['resultado'] == 2  # x > 10 mas não > 20

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
        
        assert ctx['i'] == 3
        assert ctx['j'] == 2
        assert ctx['soma'] == 6  # 3 * 2

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
        
        assert ctx['encontrado'] == 1
        assert ctx['valor'] == 5
