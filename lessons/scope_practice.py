"""Scope practice"""


def chars(msg: str) -> str:
    """return a copy of msg wo5h all instances of char removed"""
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(idx)
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"

chars(msg=a)