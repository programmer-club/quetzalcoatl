import math
import typing

import lark
import sympy
from sympy import *

from quetzalcoatl.data.expression import Expression
from quetzalcoatl.data.name import Name
from quetzalcoatl.frontends.interpret.codegen import arithmetic
from quetzalcoatl.frontends.interpret.codegen import exp_set_statement
from quetzalcoatl.frontends.interpret.codegen import find_statement
from quetzalcoatl.frontends.interpret.codegen import function_call
from quetzalcoatl.frontends.interpret.codegen import function_declaration
from quetzalcoatl.frontends.interpret.codegen import if_block
from quetzalcoatl.frontends.interpret.codegen import let_statement
from quetzalcoatl.frontends.interpret.codegen import local_var
from quetzalcoatl.frontends.interpret.codegen import make_expression
from quetzalcoatl.frontends.interpret.codegen import make_phrase
from quetzalcoatl.frontends.interpret.codegen import raw_expression
from quetzalcoatl.frontends.interpret.codegen import set_declaration
from quetzalcoatl.frontends.interpret.codegen import set_expression
from quetzalcoatl.frontends.interpret.codegen import show_phrase
from quetzalcoatl.frontends.interpret.codegen import typedef
from quetzalcoatl.frontends.interpret.codegen import unary_op

init_printing()

REGISTRY = {}
static_names = {
    'π': Name(Name.Type.EXPRESSION, math.pi),
    'e': Name(Name.Type.EXPRESSION, math.e),
    'τ': Name(Name.Type.EXPRESSION, math.tau),
    'i': Name(Name.Type.EXPRESSION, 1j),
    'print': Name(Name.Type.FUNCTION, pprint),  # TODO: map,
    # 'integrate': Name(Name.Type.FUNCTION, sympy.integrate),
    '∫': Name(Name.Type.FUNCTION, sympy.integrate),
    'd': Name(Name.Type.FUNCTION, lambda x, *args: x.diff(*args)),
    '∂': Name(Name.Type.FUNCTION, lambda x, *args: diff(x, *args)),
    'make_tuple': Name(Name.Type.FUNCTION, lambda *x: tuple(x))  # EVIL HACK
    # 'exp': exp,
}

for i in dir(sympy):
    # print(i)
    val = getattr(sympy, i)
    if callable(val):
        static_names[i] = Name(Name.Type.FUNCTION, val)


def register(key, value):
    global REGISTRY
    REGISTRY[key] = value


def get_registered(key):
    return REGISTRY[key]


do_nothing = lambda names, tree, par: par(names, tree.children[0])


def return_word(names: typing.Mapping[str, Name], tree: lark.Tree, par):
    return (
        names[tree.children[0].children[0]].val,
        names
    )


def return_named_var(names: typing.Mapping[str, Name], tree: lark.Tree, par):
    return (
        sympy.Symbol(tree.children[0].children[0]),
        names
    )


register("phrase", do_nothing)
register("expression", do_nothing)
register("atom_expression", return_word)
register("atom_variable", return_named_var)
register("atom_constant", return_word)
register("atom_set", return_word)
register("local_var", return_word)

register("make_expression", make_expression.parse)
register("unary_op", unary_op.parse)  #
register("show_phrase", show_phrase.parse)
register("make_phrase", make_phrase.parse)
register("set_declaration", set_declaration.parse)
register("if_block", if_block.parse)  #
register("function_declaration", function_declaration.parse)
register("typedef", typedef.parse)  #
register("function_call", function_call.parse)
register("let_statement", let_statement.parse)  #
register("exp_set_statement", exp_set_statement.parse)  #
register("find_statement", find_statement.parse)
register("arithmetic", arithmetic.parse)  #
register("raw_expression", raw_expression.parse)
register("set_expression", set_expression.parse)


def interpret(tree: lark.Tree):
    names: typing.Mapping[str, Name] = static_names
    for phrase in tree.children:
        output = parse(names, phrase)
        names = output[1]


def parse(names: typing.Mapping[str, Name], tree: lark.Tree) -> typing.Tuple[typing.Any, typing.Mapping[str, Name]]:
    assert not isinstance(tree, lark.Token) and hasattr(tree, 'data')
    return get_registered(tree.data)(names, tree, parse)
