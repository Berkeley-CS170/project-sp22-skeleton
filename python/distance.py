from __future__ import annotations

import dataclasses
import functools
import numbers
from typing import Union


class DoNotImplement(NotImplementedError):
    def __str__(self):
        return "Do not implement this method as it loses precision."

    def __repr__(self):
        return str(self)


@functools.total_ordering
@dataclasses.dataclass(frozen=True)
class Distance:
    value: int

    def __post_init__(self):
        assert self.value >= 0

    def __eq__(self, other: Union[numbers.Real, numbers.Complex, Distance]):
        if isinstance(other, Distance):
            return self.value == other.value
        if isinstance(other, complex):
            if other.imag == 0:
                return self == other.real
            return False
        if isinstance(other, numbers.Real):
            if other < 0:
                return False
            return self.value == other ** 2
        return False

    def __lt__(self, other: Union[numbers.Real, numbers.Complex, Distance]):
        if isinstance(other, Distance):
            return self.value < other.value
        if isinstance(other, complex):
            if other.imag == 0:
                return self < other.real
            raise ValueError
        if isinstance(other, numbers.Real):
            if other < 0:
                return True
            return self.value < other ** 2
        return False

    def __add__(self, _):
        raise DoNotImplement

    def __sub__(self, _):
        raise DoNotImplement

    def __mul__(self, _):
        raise DoNotImplement

    def __truediv__(self, _):
        raise DoNotImplement

    def __floordiv__(self, _):
        raise DoNotImplement

    def __divmod__(self, _):
        raise DoNotImplement

    def __pow__(self, pow):
        if pow == 2:
            return self.value
        raise ValueError

    def __neg__(self):
        raise DoNotImplement

    def __repr__(self):
        return f"Distance({self.value})"

    def __str__(self):
        return f"sqrt({self.value})"
