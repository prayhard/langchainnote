"""Simple agent module providing arithmetic addition functionality."""

from typing import Union

Number = Union[int, float]


def add_numbers(a: Number, b: Number) -> Number:
    """Return the arithmetic sum of ``a`` and ``b``.

    Parameters
    ----------
    a : Number
        The first addend.
    b : Number
        The second addend.

    Returns
    -------
    Number
        The sum of ``a`` and ``b``.
    """

    return a + b


__all__ = ["add_numbers"]
