from __future__ import annotations

import dataclasses
import io
from typing import Optional, TypeVar

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
        """Returns a Distance object that represents the distance between the
        two given points. We do this to avoid floating point imprecision.

        Distance objects support comparison with numbers and other distances.

        >>> Point.distance(Point(0, 0), Point(3, 4)) == 5
        True
        >>> Point.distance(Point(0, 0), Point(2, 3)) < 5
        True
        >>> Point.distance(Point(0, 0), Point(2, 3)) >= 5
        False
        """
        return Distance((first.x - second.x) ** 2 + (first.y - second.y) ** 2)

    def replace(self, *, x: Optional[int] = None, y: Optional[int] = None) -> Point:
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

    def serialize_to_string(self):
        sio = io.StringIO()
        self.serialize(sio)
        return sio.getvalue().strip()
