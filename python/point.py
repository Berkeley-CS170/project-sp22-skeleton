from __future__ import annotations

import dataclasses
import functools
from typing import Optional, TypeVar
import weakref

from distance import Distance

T = TypeVar("T")
def _coalesce(*args: Optional[T], default: T) -> T:
    for arg in args:
        if arg is not None:
            return arg
    return default

@dataclasses.dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    @staticmethod
    def distance(first: Point, second: Point):
        return Distance((first.x - second.x) ** 2 + (first.y - second.y) ** 2)

    def replace(self, *, x: Optional[int]=None, y: Optional[int]=None) -> Point:
        return Point(
            x=_coalesce(x, default=self.x),
            y=_coalesce(y, default=self.y)
        )

    @staticmethod
    def parse(line: str):
        points = line.split()
        assert len(points) == 2
        x_s, y_s = points
        return Point(x=int(x_s), y=int(y_s))

