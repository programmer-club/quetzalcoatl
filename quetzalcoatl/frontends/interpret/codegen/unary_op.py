from quetzalcoatl.frontends.interpret.codegen import arithmetic


def parse(names, tree, par):
    c1 = 0
    c2 = par(names, tree.children[1])[0]
    print(f"C2 = {c2}")
    out = -c2  # arithmetic.callmap[tree.children[0].children[0]](c1, c2)
    return (
        out, names
    )
