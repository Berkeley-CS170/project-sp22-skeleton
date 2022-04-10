from __future__ import annotations

import dataclasses
from typing import List, Iterable, Iterator

from point import Point
import parse


def _next_int(lines: Iterator[str]):
    value = next(lines)
    return int(value)


@dataclasses.dataclass
class Instance:
    grid_side_length: int
    coverage_radius: int
    penalty_radius: int
    cities: List[Point]

    @property
    def N(self):
        return len(self.cities)

    @property
    def R_s(self):
        return self.coverage_radius

    @property
    def R_p(self):
        return self.penalty_radius

    @property
    def D(self):
        return self.grid_side_length

    def valid(self):
        """Determines whether the problem instance is valid.

        A problem instance is valid if all cities are in bounds and there
        are no duplicate cities.
        """

        for city in self.cities:
            if not 0 <= city.x < self.grid_side_length:
                return False
            if not 0 <= city.y < self.grid_side_length:
                return False
        return len(set(self.cities)) == len(self.cities)

    @staticmethod
    def parse(lines: Iterable[str]) -> Instance:
        lines_iter = parse.remove_comments(lines)
        num_cities = _next_int(lines_iter)
        grid_side_length = _next_int(lines_iter)
        coverage_radius = _next_int(lines_iter)
        penalty_radius = _next_int(lines_iter)

        cities = [Point.parse(line) for line in lines_iter]
        assert num_cities == len(cities)

        instance = Instance(
            grid_side_length=grid_side_length,
            coverage_radius=coverage_radius,
            penalty_radius=penalty_radius,
            cities=cities,
        )
        assert instance.valid()
        return instance

    def serialize(self, out) -> None:
        print(len(self.cities), file=out)
        print(self.grid_side_length, file=out)
        print(self.coverage_radius, file=out)
        print(self.penalty_radius, file=out)
        for city in self.cities:
            city.serialize(out)

    def serialize_to_string(self) -> str:
        return parse.serialize_to_string_impl(self.serialize, self)
