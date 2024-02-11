"""Various stuff functions."""


def int_stuff(a: int, b: int):
    return a + b


def float_stuff(a: float, b: float):
    return a + b


def str_stuff(a: str, b: str):
    return a + b


def bool_stuff(a: bool, b: bool):
    return a and b


def list_stuff(a: list, b: list):
    return a + b


def dict_stuff(a: dict, b: dict):
    return {**a, **b}


def tuple_stuff(a: tuple, b: tuple):
    return a + b


def set_stuff(a: set, b: set):
    return a | b


def frozenset_stuff(a: frozenset, b: frozenset):
    return a | b


def bytes_stuff(a: bytes, b: bytes):
    return a + b


def bytearray_stuff(a: bytearray, b: bytearray):
    return a + b


def memoryview_stuff(a: memoryview, b: memoryview):
    return memoryview(a.tobytes() + b.tobytes())


def complex_stuff(a: complex, b: complex):
    return a + b


def exception_stuff(a: int):
    return a/0
