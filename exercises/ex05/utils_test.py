"""Testing List Utilities."""

__author__ = "730475811"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Testing for only evens."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]
    xs = [1, 5, 3]
    assert only_evens(xs) == []
    xs = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_sub() -> None:
    """Testing for subs."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]
    assert sub(xs, 10, 3) == []
    assert sub(xs, 1, -3) == []
    assert sub([], 1, 3) == []
    assert sub(xs, -1, 3) == [10, 20, 30]


def test_concat() -> None:
    """Testing for concats."""
    list_one: list[int] = [-10, -20, -30, -40]
    list_two: list[int] = [10, 20, 30, 40]
    assert concat(list_one, list_two) == [-10, -20, -30, -40, 10, 20, 30, 40]
