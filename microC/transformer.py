"""
Implementa o transformador da árvore sintática que converte entre as representações

    lark.Tree -> mc.ast.Node.

A resolução de vários exercícios requer a modificação ou implementação de vários
métodos desta classe.
"""

from typing import Callable
from lark import Transformer, v_args

from . import runtime as op
from .ast import *


def op_handler(op: Callable):
    """
    Fábrica de métodos que lidam com operações binárias na árvore sintática.

    Recebe a função que implementa a operação em tempo de execução.
    """

    def method(self, left, right):
        return BinOp(left, right, op)

    return method


@v_args(inline=True)
class McTransformer(Transformer):
    # Programa
    def program(self, *stmts):
        return Program(list(stmts))
    
    def block(self, *decls):
        return Block(list(decls))

    # Operações matemáticas básicas
    mul = op_handler(op.mul)
    div = op_handler(op.truediv)
    sub = op_handler(op.sub)
    add = op_handler(op.add)
    mod = op_handler(op.mod)

    # Operações com atribuição
    iadd = op_handler(op.iadd)
    isub = op_handler(op.isub)
    imul = op_handler(op.imul)
    itruediv = op_handler(op.itruediv)

    # Comparações
    gt = op_handler(op.gt)
    lt = op_handler(op.lt)
    ge = op_handler(op.ge)
    le = op_handler(op.le)
    eq = op_handler(op.eq)
    ne = op_handler(op.ne)

    # Operações unarias
    def not_(self, expr):
        return UnaryOp("not", expr)

    def neg(self, expr):
        return UnaryOp("-", expr)
    
    def preinc(self, expr):
        return UnaryOp("++", expr)
    
    def predec(self, expr):
        return UnaryOp("--", expr)
    
    def postinc(self, expr):
        return UnaryOp("++", expr, is_postfix=True)
    
    def postdec(self, expr):
        return UnaryOp("--", expr, is_postfix=True)

    # Outras expressões
    def or_(self, left, right):
        return Or(left, right)

    def and_(self, left, right):
        return And(left, right)

    def set(self, var, value):
        # Verifica se é acesso a array para fazer atribuição especial
        if isinstance(var, ArrayAccess):
            return ArrayAssign(var.array, var.index, value)
        return Assign(var.name, value)

    def call(self, var, *args):
        params = args[0] if args else []
        return Call(var, params)
        
    def call_params(self, *args):
        # Parâmetros de chamada: lista de expressões
        return list(args)

    def decl_params(self, *args):
        params = list(args)
        reserved = {
            "int", "char", "NULL", "return", "if", "else",
            "while", "for", "&&", "||", "void"
        }
        for p in params:
            if not isinstance(p, Var) or p.name in reserved:
                from lark.exceptions import UnexpectedToken
                # O token esperado é VAR, o token encontrado é o nome inválido
                raise UnexpectedToken(str(p.name), expected=["VAR"])
        return params

    # Comandos
    def VAR(self, token):
        name = str(token)
        return Var(name)
    
    def CHAR(self, token):
        char = str(token)
        return Literal(char[1:-1]) # tira fora as aspas

    def NUMBER(self, token):
        num = int(token)
        return Literal(num)
    
    def NULL(self):
        return Literal(None)

    # Tipos
    def type_int(self):
        return Type("int")

    def type_char(self):
        return Type("char")

    def type_void(self):
        return Type("void")

    # Declaracoes
    def var_decl(self, type_node, name, value=None):
        if type_node.name == "void":
            raise ValueError("Declaracao de variavel do tipo void nao e permitido")
        return VarDef(type_node, name.name, value)
    
    def func_decl(self, type_node, name, *rest):
        # Handle optional param_list - can be (params, body) or just (body,)
        if len(rest) == 2:
            params, body = rest
        else:
            params = None
            body = rest[0]
            
        if params is None:
            params = []
        param_names = [p.name for p in params] if params else []
        return Function(type = type_node, name=name.name, params=param_names, body=body)
    
    def array_decl(self, type_node, name, size, init_values=None):
        if type_node.name == "void":
            raise ValueError("Declaracao de array do tipo void nao e permitido")
        size_val = size.value if hasattr(size, 'value') else int(size)
        return ArrayDef(type_node, name.name, size_val, init_values)
    
    def array_init(self, *args):
        return list(args)

    def array_access(self, array, index):
        return ArrayAccess(array, index)

    # Expressoes
    def if_stmt(self, expr, then_branch, else_branch=None):
        return If(expr, then_branch, else_branch)

    def while_stmt(self, expr, stmt):
        return While(expr, stmt)
    
    def do_while_stmt(self, stmt, expr):
        return Block([stmt, While(expr, stmt)])

    def printf_stmt(self, expr):
        """
        Implementa a declaração printf, que imprime o valor de uma expressão.
        """
        return Printf(expr)
    
    def return_stmt(self, expr=None):
        return Return(expr)
    
    def expr_stmt(self, expr):
        """
        Implementa statement de expressão - simplesmente retorna a expressão.
        """
        return expr
    
    def param_list(self, *args):
        return list(args)

    def simple_param(self, type_node, name):
        return Var(name.name)

    def array_param(self, type_node, name):
        # For array parameters, we still create a Var but mark it as an array parameter
        return Var(name.name)

    def arg_list(self, *args):
        return list(args)
    
    # Subpartes do For
    def forinit(self, *args):
        # Pode ser var_decl, expr_stmt ou vazio
        return args[0] if args else None

    def forcond(self, *args):
        # Pode ser expr ou vazio
        return args[0] if args else None

    def forincr(self, *args):
        # Pode ser expr ou vazio
        return args[0] if args else None

    def for_cmd(self, init, cond, incr, body):
        # Se não houver condição, ela deve ser Literal(True)
        if cond is None:
            cond = Literal(True)
        stmts = [body]
        if incr is not None:
            stmts.append(incr)
        while_body = Block(stmts)
        while_stmt = While(cond, while_body)
        block_stmts = []
        if init is not None:
            block_stmts.append(init)
        block_stmts.append(while_stmt)
        return Block(block_stmts)

