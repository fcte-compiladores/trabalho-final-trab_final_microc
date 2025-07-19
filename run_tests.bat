@echo off
REM Script para executar testes dos exemplos MicroC no Windows

echo === Testes dos Exemplos MicroC ===

REM Verifica se pytest está disponível
pytest --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pytest não encontrado. Instalando...
    pip install pytest
)

echo 🧪 Executando testes dos exemplos...

REM Testes básicos
echo.
echo 📝 Testes básicos:
pytest tests/test_exemplos_variaveis.py -v
pytest tests/test_exemplos_arrays.py -v  
pytest tests/test_exemplos_funcoes.py -v
pytest tests/test_exemplos_estruturas_controle.py -v
pytest tests/test_exemplos_operadores.py -v
pytest tests/test_exemplos_algoritmos.py -v

REM Testes de integração
echo.
echo 🔄 Testes de integração:
pytest tests/test_todos_exemplos.py -v

REM Testes completos
echo.
echo 🚀 Executando suite completa:
pytest tests/ --full-suite -v

REM Resumo
echo.
echo 📊 Resumo dos testes:
pytest tests/ --co -q

echo.
echo ✅ Testes concluídos!
pause
