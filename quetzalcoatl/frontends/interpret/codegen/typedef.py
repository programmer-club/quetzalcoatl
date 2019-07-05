from quetzalcoatl.data.name import Name


def parse(names, tree, par):
    # BIG TODO: allow partials (e.g. typedef WeirdFunction<#a> is Bounded<#a, 2, 3>;)

    out = par(names, tree.children[1])
    names[
        tree.children[0].children[0]
    ] = Name(Name.Type.SET, out)

    return (
        out, names
    )
