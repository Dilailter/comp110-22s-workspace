"""Utilities for Lists."""

__author__ = "730475811"


def only_evens(xs: list[int]) -> list[int]:
    """Compute the even from a list."""
    only_evens = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            only_evens.append(xs[i])
        i += 1
    return only_evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Compute the sub list."""
    sub_list = []
    i: int = 0
    while i < len(xs):
        if i >= start and i < end:
            sub_list.append(xs[i])
        i += 1
    return sub_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Compute concatenated list."""
    concatenated_list = list_one
    i: int = 0
    while i < len(list_two):
        concatenated_list.append(list_two[i])
        i += 1
    return concatenated_list