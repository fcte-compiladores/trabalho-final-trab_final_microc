# MicroC - Interpretador de uma Linguagem C Simplificada

## Integrantes
- Victor Pontual - 211029601

## Introdução

Este projeto implementa um interpretador para MicroC, uma linguagem de programação simplificada baseada na sintaxe da linguagem C. O interpretador foi desenvolvido em Python utilizando a biblioteca Lark para análise sintática e implementa as principais etapas de um compilador: análise léxica, análise sintática, análise semântica e interpretação.

### Características da Linguagem MicroC

A linguagem MicroC suporta:

- **Tipos de dados**: `int`, `char` e `void`
- **Variáveis**: Declaração e inicialização de variáveis
- **Arrays**: Declaração e manipulação de arrays unidimensionais
- **Funções**: Declaração e chamada de funções com parâmetros
- **Estruturas de controle**: `if/else`, `while`, `do-while`, `for`
- **Operadores**: Aritméticos (`+`, `-`, `*`, `/`, `%`), relacionais (`<`, `>`, `<=`, `>=`, `==`, `!=`), lógicos (`&&`, `||`, `!`)
- **Operadores especiais**: Incremento/decremento (`++`, `--`) e atribuição composta (`+=`, `-=`, `*=`, `/=`)
- **Comando de saída**: `printf` para impressão de valores

### Exemplos de Código MicroC

**Hello World:**
```c
int main() {
    printf("Hello, World!");
    return 0;
}
```

**Função Recursiva (Fibonacci):**
```c
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int result = fibonacci(10);
    printf(result);
    return 0;
}
```

**Arrays e Laços:**
```c
int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int sum = 0;
    
    for (int i = 0; i < 5; i++) {
        sum += arr[i];
    }
    
    printf(sum);
    return 0;
}
```

## Instalação

### Pré-requisitos
- Python 3.10 ou superior
- Gerenciador de pacotes `uv` (recomendado) ou `pip`

### Instalação com UV
```bash
# Execute um programa MicroC
uv run python -m microC exemplos/hello.microc
```

### Opções de Execução
```bash
# Executar programa
uv run python -m microC arquivo.microc

# Ver árvore sintática
uv run python -m microC -t arquivo.microc

# Ver tokens (análise léxica)
uv run python -m microC -l arquivo.microc

# Modo interativo (REPL)
uv run python -m microC repl
```

## Exemplos

A pasta `exemplos/` contém programas organizados por categorias para demonstrar as funcionalidades do interpretador MicroC.

### Estrutura dos Exemplos

#### 📁 variaveis/
Demonstra o uso de variáveis em MicroC:
- **declaracao_basica.microc**: Declaração e inicialização de variáveis int e char
- **atribuicao_posterior.microc**: Declaração sem inicialização e atribuição posterior
- **escopo_blocos.microc**: Demonstra escopo de variáveis em blocos

#### 📁 arrays/
Exemplos de manipulação de arrays:
- **declaracao_inicializacao.microc**: Declaração e inicialização de arrays
- **manipulacao_atribuicao.microc**: Atribuição de valores em arrays e iteração
- **busca_array.microc**: Algoritmo simples de busca linear em array

#### 📁 funcoes/
Demonstra definição e uso de funções:
- **funcao_simples.microc**: Função básica com parâmetros e retorno
- **multiplas_funcoes.microc**: Múltiplas funções incluindo função void
- **funcao_recursiva.microc**: Função recursiva para cálculo de potência

#### 📁 estruturas_controle/
Estruturas de controle de fluxo:
- **condicionais.microc**: Estruturas if/else e if/else if/else
- **lacos_while.microc**: Laços while e do-while
- **lacos_for.microc**: Diferentes variações do laço for

#### 📁 operadores/
Demonstra todos os operadores suportados:
- **aritmeticos.microc**: Operadores aritméticos (+, -, *, /, %)
- **comparacao_logicos.microc**: Operadores de comparação e lógicos
- **incremento_atribuicao.microc**: Operadores ++, --, +=, -=, *=, /=

#### 📁 algoritmos/
Algoritmos mais complexos:
- **selection_sort.microc**: Algoritmo de ordenação Selection Sort
- **busca_binaria.microc**: Busca binária em array ordenado
- **kadane_algorithm.microc**: Algoritmo de Kadane para maior subsequência contígua

### Como Executar Exemplos

Para executar qualquer exemplo:

```bash
# Com UV
uv run python -m microC exemplos/categoria/arquivo.microc

# Com Python diretamente
python -m microC exemplos/categoria/arquivo.microc
```

#### Exemplos de Execução

```bash
# Executar exemplo básico
uv run python -m microC exemplos/hello.microc

# Executar exemplo de variáveis
uv run python -m microC exemplos/variaveis/declaracao_basica.microc

# Executar algoritmo de ordenação
uv run python -m microC exemplos/algoritmos/selection_sort.microc

# Ver árvore sintática de um exemplo
uv run python -m microC -t exemplos/funcoes/funcao_recursiva.microc
```

### Características dos Exemplos

Cada categoria de exemplos demonstra:

1. **Sintaxe correta** da linguagem MicroC
2. **Funcionalidades específicas** implementadas
3. **Casos de uso práticos** das construções
4. **Progressão de complexidade** dos exemplos básicos aos avançados

Os exemplos servem tanto para **testar o interpretador** quanto para **documentar a sintaxe** e **semântica** da linguagem MicroC.

## Testes

Este projeto inclui uma suíte abrangente de testes automatizados organizados por categoria.

### Estrutura dos Testes

#### 📁 test_exemplos_variaveis.py
Testa exemplos de manipulação de variáveis:
- Declaração e inicialização
- Atribuição posterior
- Escopo de blocos
- Validação de tipos

#### 📁 test_exemplos_arrays.py  
Testa exemplos de arrays:
- Declaração e inicialização de arrays
- Manipulação com atribuição
- Busca em arrays
- Verificação de limites

#### 📁 test_exemplos_funcoes.py
Testa exemplos de funções:
- Funções com parâmetros e retorno
- Funções void
- Recursão
- Escopo de variáveis

#### 📁 test_exemplos_estruturas_controle.py
Testa estruturas de controle:
- Condicionais (if/else)
- Laços (while, do-while, for)
- Estruturas aninhadas

#### 📁 test_exemplos_operadores.py
Testa operadores:
- Aritméticos (+, -, *, /, %)
- Comparação (==, !=, <, >, <=, >=)
- Lógicos (&&, ||, !)
- Incremento/decremento (++, --)
- Atribuição composta (+=, -=, *=, /=)

#### 📁 test_exemplos_algoritmos.py
Testa algoritmos complexos:
- Selection Sort
- Busca binária
- Algoritmo de Kadane
- Outros algoritmos auxiliares

#### 📁 test_todos_exemplos.py
Testes gerais e de integração:
- Execução de todos os exemplos
- Verificação da estrutura de pastas
- Validação de sintaxe geral
- Testes parametrizados por categoria

### Como Executar os Testes

#### Executar todos os testes
```bash
# Com UV (recomendado)
uv run pytest

# Com pytest diretamente
pytest tests/
```

#### Executar testes específicos
```bash
# Testar apenas variáveis
uv run pytest tests/test_exemplos_variaveis.py

# Testar apenas algoritmos
uv run pytest tests/test_exemplos_algoritmos.py

# Executar suite completa (inclui testes marcados como full_suite)
uv run pytest --full-suite

# Executar teste específico por nome/padrão
uv run pytest --maxfail=1 -k lex_numeros
```

#### Executar com verbosidade
```bash
# Ver detalhes dos testes
uv run pytest -v

# Ver output dos prints
uv run pytest -s

# Parar no primeiro erro
uv run pytest -x

# Limitar número de falhas
uv run pytest --maxfail=1
```

#### Executar testes específicos
```bash
# Testar uma função específica
uv run pytest tests/test_exemplos_funcoes.py::TestFuncoes::test_funcao_simples

# Testar uma classe específica
uv run pytest tests/test_exemplos_arrays.py::TestArrays

# Buscar testes por padrão no nome
uv run pytest -k "test_funcao"
```

### Cobertura dos Testes

A suíte de testes oferece **cobertura geral de 40%** do código-fonte, com foco nas funcionalidades principais do interpretador:

#### 📊 **Estatísticas de Cobertura por Módulo**

| Módulo | Statements | Missing | Excluded | Coverage |
|--------|------------|---------|----------|----------|
| **microC/transformer.py** | 140 | 12 | 0 | **91%** |
| **microC/parser.py** | 26 | 8 | 0 | **69%** |
| **microC/__init__.py** | 22 | 7 | 0 | **68%** |
| **microC/errors.py** | 11 | 5 | 0 | **55%** |
| **microC/ast.py** | 288 | 146 | 0 | **49%** |
| **microC/ctx.py** | 83 | 46 | 0 | **45%** |
| **microC/runtime.py** | 88 | 51 | 0 | **36%** |
| **microC/node.py** | 227 | 154 | 0 | **32%** |
| **microC/testing.py** | 397 | 298 | 0 | **25%** |
| **microC/__main__.py** | 3 | 3 | 0 | **6%** |
| **microC/cli.py** | 104 | 104 | 0 | **6%** |

#### 🎯 **Áreas com Alta Cobertura (≥60%)**

- **Transformer (91%)**: Conversão de árvore sintática para AST bem testada
- **Parser (69%)**: Análise léxica e sintática adequadamente coberta  
- **Inicialização (68%)**: Funções principais de inicialização testadas

#### ⚠️ **Áreas com Cobertura Moderada (30-59%)**

- **Errors (55%)**: Tratamento de exceções semânticas parcialmente testado
- **AST (49%)**: Estruturas de dados da árvore sintática com cobertura moderada
- **Context (45%)**: Sistema de contextos e escopos testado parcialmente
- **Runtime (36%)**: Operações em tempo de execução com teste básico
- **Node (32%)**: Nós da AST com cobertura limitada

#### 🔍 **Áreas com Baixa Cobertura (<30%)**

- **Testing (25%)**: Utilitários de teste internos pouco cobertos
- **CLI (6%)**: Interface de linha de comando não testada automaticamente
- **Main (6%)**: Ponto de entrada principal não coberto pelos testes

### Relatórios de Cobertura

Para gerar relatórios de cobertura:

```bash
# Instalar pytest-cov
uv add pytest-cov --dev

# Executar com relatório
uv run pytest tests/ --cov=microC --cov-report=html

# Visualizar relatório (abre no navegador)
start htmlcov/index.html
```

**Alternativa sem UV:**
```bash
# Instalar pytest-cov
pip install pytest-cov

# Executar com relatório
pytest tests/ --cov=microC --cov-report=html
```

### Status dos Testes

**48 testes passando** - Cobertura completa de todas as funcionalidades implementadas



## Estrutura do Código

O projeto está organizado nos seguintes módulos principais:

### `microC/grammar.lark`
Define a gramática da linguagem MicroC usando a sintaxe do Lark. Especifica as regras de produção para todas as construções da linguagem.

### `microC/parser.py`
- **Análise Léxica**: Função `lex()` que tokeniza o código fonte
- **Análise Sintática**: Função `parse()` que constrói a árvore sintática concreta e a converte para AST

### `microC/transformer.py`
Implementa a classe `McTransformer` que converte a árvore sintática do Lark para nós da AST customizada. Responsável por:
- Transformar tokens em objetos Python
- Criar nós específicos para cada construção da linguagem
- Validar sintaxe básica durante a transformação

### `microC/ast.py`
Define a estrutura da Árvore Sintática Abstrata (AST) com classes para:
- **Expressões**: `Expr`, `BinOp`, `UnaryOp`, `Var`, `Literal`, `Call`, `Assign`, etc.
- **Comandos**: `Stmt`, `VarDef`, `Function`, `If`, `While`, `Block`, `Printf`, etc.
- **Tipos**: `Type` para representar tipos de dados
- **Programa**: `Program` como nó raiz

### `microC/ctx.py`
Implementa o sistema de contextos (`Ctx`) para gerenciamento de escopos:
- Armazenamento de variáveis com tipos e valores
- Pilha de escopos para funções e blocos
- Resolução de nomes de variáveis
- Funções built-in (sqrt, clock, max)

### `microC/runtime.py`
Contém as implementações das operações em tempo de execução:
- Operações aritméticas e lógicas
- Funções de comparação com semântica específica do MicroC
- Classe `McFunction` para representar funções definidas pelo usuário
- Sistema de exceções para controle de fluxo (`McReturn`)

### `microC/errors.py`
Define exceções específicas do interpretador:
- `SemanticError` para erros semânticos
- `ForceReturn` para retorno de funções

### `microC/cli.py`
Interface de linha de comando com opções para:
- Execução de programas
- Debug (AST, tokens, árvore concreta)
- REPL interativo

### Etapas de Compilação

1. **Análise Léxica**: Realizada pelo Lark baseado na gramática
2. **Análise Sintática**: Construção da árvore sintática pelo parser LALR do Lark
3. **Transformação**: Conversão para AST customizada via `McTransformer`
4. **Análise Semântica**: Validação de tipos e escopos durante `validate_tree()`
5. **Interpretação**: Execução via método `eval()` de cada nó da AST

## Bugs/Limitações/Problemas Conhecidos

### Limitações Atuais
1. **Funções com arrays**: Passagem de arrays como parâmetros não está totalmente implementada
2. **Retorno de arrays**: Funções não podem retornar arrays
3. **Strings**: Suporte limitado a strings, apenas caracteres individuais
4. **Break/Continue**: Não implementados em laços
5. **Escopo de funções**: Funções devem ser declaradas antes do uso

### Problemas Conhecidos
1. **Mensagens de erro**: Algumas mensagens de erro poderiam ser mais descritivas
2. **Validação de tipos**: Verificação do tipo de retorno de funções não está completa
3. **Arrays multidimensionais**: Não suportados

### Melhorias Futuras
1. Implementar suporte completo para strings
2. Adicionar break e continue em laços
3. Melhorar mensagens de erro com localização precisa
4. Implementar otimizações básicas na interpretação
5. Adicionar mais funções built-in (abs, min, etc.)
6. Suporte para structs/records simples

## Referências

1. **Nystrom, R.** *Crafting Interpreters*. Genever Benning, 2021.  
   Disponível em: https://craftinginterpreters.com/  
   *Referência fundamental para a arquitetura do interpretador, implementação de árvores sintáticas abstratas e técnicas de interpretação.*

2. **Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D.** *Compilers: Principles, Techniques, and Tools* (2ª ed.). Pearson, 2006.  
   *Base teórica para análise léxica, análise sintática, análise semântica e técnicas de compilação.*

3. **Kernighan, B. W., & Ritchie, D. M.** *The C Programming Language* (2ª ed.). Prentice Hall, 1988.  
   *Referência para a sintaxe e semântica da linguagem C que inspirou o MicroC.*

### Ferramentas e Bibliotecas

4. **Lark Parser Documentation**. Disponível em: https://lark-parser.readthedocs.io/  
   *Documentação oficial da biblioteca Lark utilizada para análise sintática LALR e construção de gramáticas.*

5. **Python Software Foundation**. *Python Language Reference*. Disponível em: https://docs.python.org/3/  
   *Documentação oficial do Python 3.13+ utilizado na implementação do interpretador.*

6. **Pytest Documentation**. Disponível em: https://docs.pytest.org/  
   *Framework de testes utilizado para a suíte de testes automatizados do projeto.*