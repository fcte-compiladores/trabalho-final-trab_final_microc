from abc import ABC
from dataclasses import dataclass
from typing import Callable, Optional
from .runtime import McFunction, McReturn
from .errors import SemanticError

from .ctx import Ctx

# Declaramos nossa classe base num módulo separado para esconder um pouco de
# Python relativamente avançado de quem não se interessar pelo assunto.
#
# A classe Node implementa um método `pretty` que imprime as árvores de forma
# legível. Também possui funcionalidades para navegar na árvore usando cursores
# e métodos de visitação.
from .node import Node, Cursor


#
# TIPOS BÁSICOS
#

# Tipos de valores que podem aparecer durante a execução do programa
Value = int | None


@dataclass
class Type(Node):
    """
    Representa um tipo de dados.
    
    Ex.: int, void
    """
    name: str

    def eval(self, ctx: Ctx):
        return self.name


class Expr(Node, ABC):
    """
    Classe base para expressões.

    Expressões são nós que podem ser avaliados para produzir um valor.
    Também podem ser atribuídos a variáveis, passados como argumentos para
    funções, etc.
    """


class Stmt(Node, ABC):
    """
    Classe base para comandos.

    Comandos são associdos a construtos sintáticos que alteram o fluxo de
    execução do código ou declaram elementos como classes, funções, etc.
    """


@dataclass
class Program(Node):
    stmts: list[Stmt]

    def eval(self, ctx: Ctx):
        for stmt in self.stmts:
            stmt.eval(ctx)

    def validate_self(self, cursor: Cursor):
        pass

#
#
@dataclass
class BinOp(Expr):
    """
    Uma operação infixa com dois operandos.

    Ex.: x + y, 2 * x, 3.14 > 3 and 3.14 < 4
    """

    left: Expr
    right: Expr
    op: Callable[[Value, Value], Value]

    def eval(self, ctx: Ctx):
        if isinstance(self.left, str) or isinstance(self.right, str):
            raise TypeError("operações binárias não suportam strings")
        left_value = self.left.eval(ctx)
        right_value = self.right.eval(ctx)
        return self.op(left_value, right_value)


@dataclass
class Var(Expr):
    name: str

    def eval(self, ctx: Ctx):
        try:
            return ctx[self.name]
        except KeyError:
            raise NameError(f"variável {self.name} não existe!")

    def validate_self(self, cursor: Cursor):
        reserved = {
            "NULL", "return","if", "else",
            "while", "for", "&&", "||", 
            "void", "int", 
        }
        if self.name in reserved:
            raise SemanticError("nome inválido", token=self.name)

@dataclass
class Literal(Expr):
    """
    Representa valores literais no código, ex.: strings, booleanos,
    números, etc.

    Ex.: "Hello, world!", 42, 3.14, true, nil
    """

    value: Value

    def eval(self, ctx: Ctx):
        return self.value


@dataclass
class And(Expr):
    """
    Uma operação infixa com dois operandos.

    Ex.: x and y
    """
    left: Expr
    right: Expr

    def eval(self, ctx: Ctx):
        left = self.left.eval(ctx)
        if not left:
            return 0
        right = self.right.eval(ctx)
        return 1 if right else 0
    

@dataclass
class Or(Expr):
    """
    Uma operação infixa com dois operandos.
    Ex.: x or y
    """
    left: Expr
    right: Expr

    def eval(self, ctx: Ctx):
        left = self.left.eval(ctx)
        if left:
            return 1
        right = self.right.eval(ctx)
        return 1 if right else 0



@dataclass
class UnaryOp(Expr):
    op: str
    params: Expr
    is_postfix: bool = False

    def eval(self, ctx: Ctx):
        val = self.params.eval(ctx)
        if self.op == "-":
            return -val
        
        elif self.op == "not":
            return 1 if not val else 0
        
        elif self.op == "++":
            if self.is_postfix:
                result = val
                self.params.eval(ctx)
                return result + 1
            return val + 1
        
        elif self.op == "--":
            if self.is_postfix:
                result = val
                self.params.eval(ctx)
                return result - 1
            return val - 1


@dataclass
class Call(Expr):
    callee: Expr
    params: list[Expr]

    def eval(self, ctx: Ctx):
        func = self.callee.eval(ctx)
        args = [param.eval(ctx) for param in self.params]
        from .runtime import McClass, McInstance
        if isinstance(func, McClass):
            return McInstance(func)
        if callable(func):
            return func(*args)
        raise TypeError(f"{self.callee} não é uma função!")



@dataclass
class Assign(Expr):
    """
    Atribuição de variável.

    Ex.: int x = 42
    """
    name: str
    value: Expr

    def eval(self, ctx: Ctx):
        val = self.value.eval(ctx)
        var_type = ctx.get_type(self.name)
        if var_type.name == "char" and isinstance(val, int):
            val = chr(val)
        elif var_type.name == "int" and isinstance(val, str):
            val = ord(val)
        ctx[self.name] = val
        return val

#
# COMANDOS
#

@dataclass
class Return(Stmt):
    value: Optional[Expr] = None

    def eval(self, ctx):
        val = self.value.eval(ctx) if self.value else None
        from .runtime import McReturn
        raise McReturn(val)
    
@dataclass
class Printf(Stmt):
    expr: Expr

    def eval(self, ctx: Ctx):
        value = self.expr.eval(ctx)
        tipo = None
        if isinstance(self.expr, Var):
            tipo = ctx.get_type(self.expr.name)
            if tipo.name == "void":
                raise TypeError("printf não pode imprimir valores do tipo void")
            if tipo.name == "int" and isinstance(value, list):
                raise TypeError("printf não pode imprimir arrays de inteiros diretamente, use um loop :)")
        from .runtime import print
        print(value)

@dataclass
class VarDef(Stmt):
    type: Type
    name: str
    value: Expr | None = None

    def eval(self, ctx: Ctx):
        if self.value is not None:
            val = self.value.eval(ctx)
            if self.type.name == "int" and isinstance(val, str):
                val = ord(val)
            elif self.type.name == "char" and isinstance(val, int):
                val = chr(val)
        else:
            if self.type.name == "int":
                val = 0
            elif self.type.name == "char":
                val = '\0'
            else:
                val = None
        ctx.var_def(self.type, self.name, val)

    def validate_self(self, cursor: Cursor):
        reserved = {
            "NULL", "return", "if", "else",
            "while", "for", "&&", "||", 
            "void", "int", "char",
        }
        if self.name in reserved:
            raise SemanticError("nome inválido", token=self.name)


@dataclass
class If(Stmt):
    """
    Representa uma instrução condicional.

    Ex.: if (x > 0) { ... } else { ... }
    """
    expr: Expr
    then_branch: Stmt
    else_branch: Optional[Stmt] = None

    def eval(self, ctx: Ctx):
        cond = self.expr.eval(ctx)
        if cond:
            return self.then_branch.eval(ctx)
        elif self.else_branch is not None:
            return self.else_branch.eval(ctx)

@dataclass
class While(Stmt):
    """
    Representa um laço de repetição.

    Ex.: while (x > 0) { ... }
    """
    expr : Expr
    stmt : Stmt

    def eval(self, ctx: Ctx):
        while self.expr.eval(ctx):
            self.stmt.eval(ctx)


@dataclass
class Block(Node):
    stmts: list[Stmt]

    def eval(self, ctx: Ctx):
        new_ctx = ctx.push({})
        for stmt in self.stmts:
            stmt.eval(new_ctx)
        env, ctx = new_ctx.pop()

    def validate_self(self, cursor: Cursor):
        var_names = [stmt.name for stmt in self.stmts if isinstance(stmt, VarDef)]
        seen = set()
        for name in var_names:
            if name in seen:
                raise SemanticError("variável duplicada em bloco", token=name)
            seen.add(name)


@dataclass
class Function(Stmt):
    type: Type
    name: str
    params: list[str]
    body: Stmt

    def eval(self, ctx: "Ctx"):
        stmts = self.body.stmts if hasattr(self.body, "stmts") else [self.body]
        func = McFunction(self.type.name, self.name, self.params, stmts, ctx)
        ctx.var_def(self.type, self.name, func)
        return func

    def validate_self(self, cursor: Cursor):
        if len(self.params) != len(set(self.params)):
            # Descobre qual parâmetro está duplicado
            seen = set()
            for p in self.params:
                if p in seen:
                    raise SemanticError("parâmetro duplicado", token=p)
                seen.add(p)
        # Verifica se algum VarDef no corpo tem nome igual a algum parâmetro
        param_set = set(self.params)
        # Procura VarDef no corpo
        if hasattr(self.body, "stmts"):
            for stmt in self.body.stmts:
                if isinstance(stmt, VarDef) and stmt.name in param_set:
                    raise SemanticError("variável colide com parâmetro", token=stmt.name)

@dataclass
class ArrayDef(Stmt):
    type: Type
    name: str
    size: int
    init_values: Optional[list[Expr]] = None

    def eval(self, ctx: Ctx):
        if self.type.name == "char":
            if self.init_values:
                chars = [str(expr.eval(ctx)) for expr in self.init_values]
                while len(chars) < self.size - 1:
                    chars.append('\0')
                chars.append('\0')
                value = ''.join(chars[:self.size])
            else:
                value = '\0' * self.size
            ctx[self.name] = value
        else:
            if self.init_values:
                values = [expr.eval(ctx) for expr in self.init_values]
                while len(values) < self.size:
                    values.append(0)
            else:
                values = [0] * self.size
            ctx[self.name] = values

    def validate_self(self, cursor: Cursor):
        reserved = {
            "NULL", "return","if", "else",
            "while", "for", "&&", "||", 
            "void", "int",
        }
        if self.name in reserved:
            raise SemanticError("nome inválido", token=self.name)

@dataclass
class ArrayAccess(Expr):
    array: Expr
    index: Expr

    def eval(self, ctx: Ctx):
        arr = self.array.eval(ctx)
        idx = self.index.eval(ctx)
        if not isinstance(arr, list):
            raise TypeError(f"{self.array} não é um array!")
        if not isinstance(idx, int):
            raise TypeError("Índice deve ser um inteiro!")
        if idx < 0 or idx >= len(arr):
            raise IndexError(f"Índice {idx} fora dos limites do array!")
        return arr[idx]

@dataclass
class ArrayAssign(Expr):
    array: Expr
    index: Expr
    value: Expr

    def eval(self, ctx: Ctx):
        arr = self.array.eval(ctx)
        idx = self.index.eval(ctx)
        val = self.value.eval(ctx)
        if not isinstance(arr, list):
            raise TypeError(f"{self.array} não é um array!")
        if not isinstance(idx, int):
            raise TypeError("Índice deve ser um inteiro!")
        if idx < 0 or idx >= len(arr):
            raise IndexError(f"Índice {idx} fora dos limites do array!")
        arr[idx] = val
        return val