#!/bin/bash
# Script para executar testes dos exemplos MicroC

echo "=== Testes dos Exemplos MicroC ==="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir com cor
print_color() {
    echo -e "${2}${1}${NC}"
}

# Verifica se pytest está disponível
if ! command -v pytest &> /dev/null; then
    print_color "❌ pytest não encontrado. Instalando..." $RED
    pip install pytest
fi

print_color "🧪 Executando testes dos exemplos..." $BLUE

# Testes básicos (sem full-suite)
print_color "\n📝 Testes básicos:" $YELLOW
pytest tests/test_exemplos_variaveis.py -v
pytest tests/test_exemplos_arrays.py -v  
pytest tests/test_exemplos_funcoes.py -v
pytest tests/test_exemplos_estruturas_controle.py -v
pytest tests/test_exemplos_operadores.py -v
pytest tests/test_exemplos_algoritmos.py -v

# Testes de integração
print_color "\n🔄 Testes de integração:" $YELLOW
pytest tests/test_todos_exemplos.py -v

# Testes completos (com full-suite)
print_color "\n🚀 Executando suite completa:" $YELLOW
pytest tests/ --full-suite -v

# Resumo
print_color "\n📊 Resumo dos testes:" $GREEN
pytest tests/ --co -q | grep -E "test session starts|collected"

print_color "\n✅ Testes concluídos!" $GREEN
