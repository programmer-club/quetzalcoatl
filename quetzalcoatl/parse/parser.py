import lark
import os

GRAMMAR_FILE = os.path.join("..", "resx", "GRAMMAR.lark")

with open(GRAMMAR_FILE) as file:
    lark_parser = lark.lark.Lark(file.read(), propagate_positions=True)


def parse(text: str):
    print(lark_parser.parse(text))
