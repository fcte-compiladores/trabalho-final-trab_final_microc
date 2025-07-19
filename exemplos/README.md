# Exemplos MicroC

Esta pasta contém exemplos organizados por categorias para demonstrar as funcionalidades do interpretador MicroC.

## Estrutura dos Exemplos

### 📁 variaveis/
Demonstra o uso de variáveis em MicroC:
- **declaracao_basica.microc**: Declaração e inicialização de variáveis int e char
- **atribuicao_posterior.microc**: Declaração sem inicialização e atribuição posterior
- **escopo_blocos.microc**: Demonstra escopo de variáveis em blocos

### 📁 arrays/
Exemplos de manipulação de arrays:
- **declaracao_inicializacao.microc**: Declaração e inicialização de arrays
- **manipulacao_atribuicao.microc**: Atribuição de valores em arrays e iteração
- **busca_array.microc**: Algoritmo simples de busca linear em array

### 📁 funcoes/
Demonstra definição e uso de funções:
- **funcao_simples.microc**: Função básica com parâmetros e retorno
- **multiplas_funcoes.microc**: Múltiplas funções incluindo função void
- **funcao_recursiva.microc**: Função recursiva para cálculo de potência

### 📁 estruturas_controle/
Estruturas de controle de fluxo:
- **condicionais.microc**: Estruturas if/else e if/else if/else
- **lacos_while.microc**: Laços while e do-while
- **lacos_for.microc**: Diferentes variações do laço for

### 📁 operadores/
Demonstra todos os operadores suportados:
- **aritmeticos.microc**: Operadores aritméticos (+, -, *, /, %)
- **comparacao_logicos.microc**: Operadores de comparação e lógicos
- **incremento_atribuicao.microc**: Operadores ++, --, +=, -=, *=, /=

### 📁 algoritmos/
Algoritmos mais complexos:
- **selection_sort.microc**: Algoritmo de ordenação Selection Sort
- **busca_binaria.microc**: Busca binária em array ordenado
- **kadane_algorithm.microc**: Algoritmo de Kadane para maior subsequência contígua

## Como Executar

Para executar qualquer exemplo:

```bash
# Com UV
uv run python -m microC exemplos/categoria/arquivo.microc

# Com Python diretamente
python -m microC exemplos/categoria/arquivo.microc
```

### Exemplos de Execução

```bash
# Executar exemplo de variáveis
uv run python -m microC exemplos/variaveis/declaracao_basica.microc

# Executar algoritmo de ordenação
uv run python -m microC exemplos/algoritmos/selection_sort.microc

# Ver árvore sintática de um exemplo
uv run python -m microC -t exemplos/funcoes/funcao_recursiva.microc
```

## Características Demonstradas

Cada categoria de exemplos demonstra:

1. **Sintaxe correta** da linguagem MicroC
2. **Funcionalidades específicas** implementadas
3. **Casos de uso práticos** das construções
4. **Progressão de complexidade** dos exemplos básicos aos avançados

Os exemplos servem tanto para **testar o interpretador** quanto para **documentar a sintaxe** e **semântica** da linguagem MicroC.
