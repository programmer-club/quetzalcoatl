from quetzalcoatl.data.name import Name


def parse(names, tree, par):  # TODO: let typed
    set_ = tree.children[0]
    out = par(names, set_.children[1])
    names[
        set_.children[0].children[0].children[0]
    ] = Name(Name.Type.EXPRESSION, out)

    return (
        out, names
    )
