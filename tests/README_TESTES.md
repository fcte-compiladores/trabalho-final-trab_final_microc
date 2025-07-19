# Testes para Exemplos MicroC

Este diretório contém testes automatizados para todos os exemplos de código MicroC organizados por categoria.

## Estrutura dos Testes

### 📁 test_exemplos_variaveis.py
Testa exemplos de manipulação de variáveis:
- Declaração e inicialização
- Atribuição posterior
- Escopo de blocos
- Validação de tipos

### 📁 test_exemplos_arrays.py  
Testa exemplos de arrays:
- Declaração e inicialização de arrays
- Manipulação com atribuição
- Busca em arrays
- Verificação de limites

### 📁 test_exemplos_funcoes.py
Testa exemplos de funções:
- Funções com parâmetros e retorno
- Funções void
- Recursão
- Escopo de variáveis

### 📁 test_exemplos_estruturas_controle.py
Testa estruturas de controle:
- Condicionais (if/else)
- Laços (while, do-while, for)
- Estruturas aninhadas

### 📁 test_exemplos_operadores.py
Testa operadores:
- Aritméticos (+, -, *, /, %)
- Comparação (==, !=, <, >, <=, >=)
- Lógicos (&&, ||, !)
- Incremento/decremento (++, --)
- Atribuição composta (+=, -=, *=, /=)

### 📁 test_exemplos_algoritmos.py
Testa algoritmos complexos:
- Selection Sort
- Busca binária
- Algoritmo de Kadane
- Outros algoritmos auxiliares

### 📁 test_todos_exemplos.py
Testes gerais e de integração:
- Execução de todos os exemplos
- Verificação da estrutura de pastas
- Validação de sintaxe geral
- Testes parametrizados por categoria

## Como Executar os Testes

### Executar todos os testes
```bash
# Com pytest
pytest tests/

# Com UV
uv run pytest tests/
```

### Executar testes específicos
```bash
# Testar apenas variáveis
pytest tests/test_exemplos_variaveis.py

# Testar apenas algoritmos
pytest tests/test_exemplos_algoritmos.py

# Executar suite completa (inclui testes marcados como full_suite)
pytest tests/ --full-suite
```

### Executar com verbosidade
```bash
# Ver detalhes dos testes
pytest tests/ -v

# Ver output dos prints
pytest tests/ -s

# Parar no primeiro erro
pytest tests/ -x
```

### Executar testes específicos
```bash
# Testar uma função específica
pytest tests/test_exemplos_funcoes.py::TestFuncoes::test_funcao_simples

# Testar uma classe específica
pytest tests/test_exemplos_arrays.py::TestArrays
```

## Tipos de Testes Implementados

### 1. **Testes de Parse**
- Verificam se o código pode ser analisado sintaticamente
- Validam a estrutura da AST
- Verificam validação semântica

### 2. **Testes de Execução**
- Executam o código e verificam resultados
- Testam estado final das variáveis
- Verificam comportamento esperado

### 3. **Testes de Integração**
- Testam múltiplos exemplos juntos
- Verificam estrutura geral do projeto
- Validam consistência entre exemplos

### 4. **Testes Parametrizados**
- Executam o mesmo teste para múltiplas categorias
- Verificam consistência entre diferentes exemplos
- Permitem cobertura abrangente com menos código

## Cobertura dos Testes

Os testes cobrem:

✅ **Sintaxe**: Todos os exemplos devem ser parseáveis  
✅ **Semântica**: Validação de tipos e escopos  
✅ **Execução**: Exemplos devem executar corretamente  
✅ **Funcionalidades**: Todas as features do MicroC  
✅ **Casos extremos**: Situações limite e de erro  
✅ **Integração**: Interação entre componentes  

## Marcadores de Teste

- `@pytest.mark.full_suite`: Testes que requerem a flag `--full-suite`
- `@pytest.mark.parametrize`: Testes parametrizados para múltiplos casos

## Relatórios

Para gerar relatórios de cobertura:

```bash
# Instalar coverage
pip install pytest-cov

# Executar com relatório
pytest tests/ --cov=microC --cov-report=html
```

## Contribuindo

Ao adicionar novos exemplos:

1. **Crie testes correspondentes** nos arquivos apropriados
2. **Mantenha a estrutura** de teste existente
3. **Teste parsing, validação e execução**
4. **Documente comportamento esperado**
5. **Use assertions claras** e mensagens de erro úteis
