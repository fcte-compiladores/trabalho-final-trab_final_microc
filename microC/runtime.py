import builtins
from dataclasses import dataclass
from operator import add, ge, gt, le, lt, mul, neg, not_, sub, truediv, mod, iadd, isub, imul, itruediv
from typing import TYPE_CHECKING

from .ctx import Ctx

if TYPE_CHECKING:
    from .ast import Stmt, Value

__all__ = [
    "add",
    "eq",
    "ge",
    "gt",
    "le",
    "lt",
    "mul",
    "ne",
    "neg",
    "not_",
    "print",
    "show",
    "sub",
    "truthy",
    "truediv",
    "mod",
    "iadd",
    "isub",
    "imul",
    "itruediv",
    "increment",
    "decrement",
]

def eq(a, b):
    # Tipos diferentes nunca são iguais em MicroC
    if type(a) != type(b):
        return False
    return a == b

def ne(a, b):
    # Tipos diferentes sempre são diferentes em MicroC
    if type(a) != type(b):
        return True
    return a != b

def increment(a: "Value") -> "Value":
    """
    Incrementa o valor de a, retornando o novo valor.
    """
    if isinstance(a, int):
        return a + 1
    else:
        raise TypeError(f"Tipo esperado para incremento é int, mas foi passado {type(a)}")

def decrement(a: "Value") -> "Value":
    """
    Decrementa o valor de a, retornando o novo valor.
    """
    if isinstance(a, int):
        return a - 1
    else:
        raise TypeError(f"Tipo esperado para decremento é int, mas foi passado {type(a)}")


@dataclass
class McFunction:
    type: str
    name: str
    args: list[str]
    body: list  # lista de Stmt
    ctx: Ctx

    def __call__(self, *args):
        # Cria novo escopo para a chamada
        env = dict(zip(self.args, args, strict=True))
        local_ctx = self.ctx.push(env)
        try:
            for stmt in self.body:
                stmt.eval(local_ctx)
        except McReturn as e:
            return e.value
        return None


class McReturn(Exception):
    """
    Exceção para retornar de uma função MicroC.
    """

    def __init__(self, value):
        self.value = value
        super().__init__()


class McError(Exception):
    """
    Exceção para erros de execução MicroC.
    """

nan = None
inf = None


def print(value: "Value"):
    """
    Imprime um valor MicroC.
    """
    builtins.print(show(value))


import types

def show(value):
    # None -> NULL
    if value is None:
        return "NULL"
    # Arrays
    if isinstance(value, list):
        if value and all(isinstance(elem, str) and len(elem) == 1 for elem in value):
            # Imprime até o primeiro '\0'
            s = ""
            for c in value:
                if c == '\0':
                    break
                s += c
            return s
        return "<array>"
    # Booleanos
    if value is True:
        return "true"
    if value is False:
        return "false"
    # McFunction
    if isinstance(value, McFunction):
        return f"<fn {value.name}>"
    # Função nativa do Python
    import types
    if isinstance(value, types.BuiltinFunctionType):
        return "<native fn>"
    # Fallback
    return str(value)


def show_repr(value: "Value") -> str:
    """
    Mostra um valor MicroC, mas coloca aspas em strings.
    """
    if isinstance(value, str):
        return f'"{value}"'
    return show(value)


def truthy(value: "Value") -> bool:
    """
    Converte valor MicroC para booleano segundo a semântica do MicroC.
    """
    if value is None or value is False:
        return False
    return True


