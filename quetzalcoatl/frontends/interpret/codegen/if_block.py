def parse_fnbody(names, tree, par):
    res = None

    for i in tree.children:
        res, names = par(names, i)

    return (
        res, names
    )


def parse(names, tree, par):
    if_ = tree.children[0]
    if len(tree.children) > 1:
        else_ = tree.children[1]
    else:
        else_ = None

    value, names = par(names, if_.children[0])  # TODO: this everywhere (value,names = par....)

    if value:
        return parse_fnbody(names, if_.children[1], par)
    else:
        if else_:
            return parse_fnbody(names, else_.children[0], par)
        else:
            return (
                None, names
            )
