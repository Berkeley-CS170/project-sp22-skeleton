from __future__ import annotations

import dataclasses
from typing import Optional, TypeVar

from .distance import Distance
from . import parse

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

    def distance_sq(self: Point, second: Point):
        """Returns the squared distance between two points.

        Comparing squared distances avoids floating point imprecision. In
        practice, for the small distances we are dealing with, there should be
        no imprecision with regular square roots if floating point operations
        are implemented in accordance with the IEEE 754 standard.

        >>> Point.distance_sq(Point(0, 0), Point(3, 4))
        25
        """
        dx = self.x - second.x
        dy = self.y - second.y
        return ((dx ** 2) + (dy ** 2))

    def distance_obj(self: Point, second: Point):
        """Returns a Distance object that represents the distance between the
        two given points.

        Internally, the Distance object stores the squared distance between two
        points. When a Distance object is compared with a number, we square the
        number. Comparing squared distances avoids floating point imprecision.

        This method may be more convenient than distance_sq as there is no need
        to manually square the other operand of comparison as the Distance
        object squares it for you.

        There may be bugs in the Distance implementation. Use at your own risk.

        >>> Point.distance_obj(Point(0, 0), Point(3, 4)) == 5
        True
        >>> Point.distance_obj(Point(0, 0), Point(2, 3)) < 5
        True
        >>> Point.distance_obj(Point(0, 0), Point(2, 3)) >= 5
        False
        """
        return Distance((self.x - second.x) ** 2 + (self.y - second.y) ** 2)

    def replace(self, *, x: Optional[int] = None, y: Optional[int] = None) -> Point:
        """Constructs a new Point with the parameters passed replaced.

        >>> point = Point(1, 2)
        >>> point.replace(y=3)
        Point(x=1, y=3)
        >>> point = Point(1, 2)
        >>> point.replace(x=5)
        Point(x=5, y=2)
        """
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

    def serialize(self, out):
        print(self.x, self.y, file=out)

    def serialize_to_string(self) -> str:
        return parse.serialize_to_string_impl(self.serialize, self)
