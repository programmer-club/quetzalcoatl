import ast


def parse(names, tree, par):
    return (
        ast.literal_eval(tree.children[0]),
        names
    )
