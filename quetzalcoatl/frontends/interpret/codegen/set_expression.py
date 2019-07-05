import ast


def parse(names, tree, par):
    return (  # TODO: this fuckin bullshit
        ast.literal_eval(tree.children[0]),
        names
    )
