import operator

callmap = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    '!=': operator.ne,
    '==': operator.eq,
    '..': range,  # TODO: custom range that allows for infinity
}


def parse(names, tree, par):
    c1 = par(names, tree.children[0])[0]
    c2 = par(names, tree.children[2])[0]
    out = callmap[tree.children[1].children[0]](c1, c2)
    return (
        out, names
    )
