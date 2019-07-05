from sympy.solvers import solve


def parse(names, tree, par):
    equation, names = par(names, tree.children[0])  # LtR evaluation
    value, names = par(names, tree.children[1])
    for_, names = par(names, tree.children[2])

    result = solve(equation - value, for_)

    return (
        result,
        names
    )
