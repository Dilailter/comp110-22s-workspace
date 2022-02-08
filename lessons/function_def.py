"""An example of function definitions."""
# line 5 is the signiture line/"contract"


def my_max(a: int, b: int) -> int:
    # the docstring is the describtion
    """Return the largest argument."""
    if a >= b:
        return a
    else:
        return b
# line 9-13 is the body block


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)