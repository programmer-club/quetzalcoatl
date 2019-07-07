from quetzalcoatl.data.name import Name


def parse(names, tree, par):
    expr = par(names, tree.children[3])
    names[tree.children[0].children[0]] = Name(Name.Type.FUNCTION, expr)
    # TODO: add local variables by parsing type
    # TODO: add types to function value

    return (
        expr,
        names
    )
