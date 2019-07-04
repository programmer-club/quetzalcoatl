from quetzalcoatl.parse.parser import parse
import os

if __name__ == "__main__":
    # accumulate_args()
    with open(os.path.join("..", "examples", "spec.qz")) as f:
        parse(f.read())
