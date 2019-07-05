from lark import lark
import operator
import typing


class Expression:
    def __init__(self, tree: typing.Union[lark.Tree, type(None)]):
        if tree is None:
            return
        self.left = tree.children[0].children[0]
        self.op = lambda a, b: None
        self.right = None

    @staticmethod
    def from_(left, op, right):
        self = Expression(None)
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"{self.left} {self.op} {self.right}"

    def __add__(self, other):
        return Expression.from_(self, operator.add, other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Expression.from_(self, operator.sub, other)

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        return Expression.from_(self, operator.mul, other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return Expression.from_(self, operator.truediv, other)

    def __rtruediv__(self, other):
        return self / other
