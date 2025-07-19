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
# Clone o repositório
git clone <url-do-repositorio>
cd trabalho-final-trab_final_microc

# Instale as dependências
uv sync

# Execute um programa MicroC
uv run python -m microC exemplos/hello.microc
```

### Instalação com PIP
```bash
# Clone o repositório
git clone <url-do-repositorio>
cd trabalho-final-trab_final_microc

# Instale as dependências
pip install -r requirements.txt

# Execute um programa MicroC
python -m microC exemplos/hello.microc
```

### Opções de Execução
```bash
# Executar programa
python -m microC arquivo.microc

# Ver árvore sintática
python -m microC -t arquivo.microc

# Ver tokens (análise léxica)
python -m microC -l arquivo.microc

# Modo interativo (REPL)
python -m microC repl
```

## Exemplos

A pasta `exemplos/` contém programas de exemplo com diferentes níveis de complexidade:

- **hello.microc**: Programa básico "Hello World"
- **fibonacci.microc**: Implementação recursiva da sequência de Fibonacci
- **factorial.microc**: Cálculo do fatorial usando recursão
- **arrays.microc**: Manipulação básica de arrays
- **bubble_sort.microc**: Algoritmo de ordenação bubble sort

## Referências

1. **Crafting Interpreters** por Robert Nystrom - Referência principal para a arquitetura do interpretador e implementação de árvores sintáticas abstratas
2. **Lark Parser** - Biblioteca Python utilizada para análise sintática e construção de gramáticas
3. **Compiladores: Princípios, Técnicas e Ferramentas** (Livro do Dragão) - Base teórica para análise léxica, sintática e semântica
4. **Linguagem C (K&R)** - Referência para a sintaxe e semântica da linguagem C que inspirou o MicroC

**Contribuições originais:**
- Implementação da validação semântica com verificação de tipos
- Sistema de contextos para gerenciamento de escopos
- Suporte para arrays com verificação de limites
- Operadores de incremento/decremento e atribuição composta
- Estrutura do-while e validações específicas para MicroC

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

## Critérios

Cada trabalho começa com 100% e pode receber penalizações ou bônus de acordo com
os critérios abaixo:

- Ausência do README: -50%
- Instruções de instalação não funcionam: até -20%
- Referências não atribuídas ou falta de referâncias: -10%
- Código confuso ou mal organizado: até -15%
- Falta de clareza em apresentar as técnicas e etapas de compilação: -15%
- Bugs e limitações sérias na implementação: até -25%
- Escopo reduzido, ou implementação insuficiente: até 25%
- Uso de código não atribuído/plágio: até -100%
- Repositório bem estruturado e organizado: até 10%
- Linguagem com conceitos originais/interessantes: até +15%
- Testes unitários: até +15%, dependendo da cobertura

Após aplicar todos os bônus, a nota é truncada no intervalo 0-100%. 
