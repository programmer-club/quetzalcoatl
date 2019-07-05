import enum


class Name:  # TODO: set this name is a part of
    class Type(enum.Enum):
        VARIABLE = 1  # a
        EXPRESSION = 2  # $a
        SET = 3  # #a
        SET_INSTANCE = 4  # #a
        CONSTANT = 5  # @a
        FUNCTION = 6

    def __init__(self, ty: Type, val):
        self.ty = ty
        self.val = val
