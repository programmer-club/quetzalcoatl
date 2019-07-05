def parse(names, tree, par):
    # TODO: make this not an evil haxxor move
    right, names = par(names, tree.children[1])
    return (
        names[tree.children[0].children[0]].val(
            right
        ),
        names
    )
