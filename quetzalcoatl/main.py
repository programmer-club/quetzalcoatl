from quetzalcoatl.parse.parser import parse
import os

if __name__ == "__main__":
    # accumulate_args()

    from quetzalcoatl.frontends.interpret import interpret
    # quetzalcoatl.frontends.interpret.interpret.interpret(tree)
    with open(os.path.join("..", "examples", "spec.qz")) as f:
        tree = parse(f.read())
        interpret.interpret(tree)
