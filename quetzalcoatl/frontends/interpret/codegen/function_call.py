def parse(names, tree, par):
    right = []
    if len(tree.children) > 1:
        for i in tree.children[1:]:
            r, names = par(names, i)
            right.append(r)

    return (
        names[tree.children[0].children[0]].val(
            *right
        ),
        names
    )
