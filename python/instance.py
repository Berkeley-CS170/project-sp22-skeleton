from __future__ import annotations

import dataclasses
import io
from typing import Iterable, Iterator, List, TYPE_CHECKING

from point import Point
from svg import SVGGraphic

if TYPE_CHECKING:
    from visualize import VisualizationConfig


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
    def parse(lines: Iterable[str]):
        lines = iter(lines)
        num_cities = _next_int(lines)
        grid_side_length = _next_int(lines)
        coverage_radius = _next_int(lines)
        penalty_radius = _next_int(lines)

        cities = [Point.parse(line) for line in lines]
        assert num_cities == len(cities)

        instance = Instance(
            grid_side_length=grid_side_length,
            coverage_radius=coverage_radius,
            penalty_radius=penalty_radius,
            cities=cities,
        )
        assert instance.valid()
        return instance

    def serialize(self, out):
        print(len(self.cities), file=out)
        print(self.grid_side_length, file=out)
        print(self.coverage_radius, file=out)
        print(self.penalty_radius, file=out)
        for city in self.cities:
            city.serialize(out)

    def serialize_to_string(self):
        sio = io.StringIO()
        self.serialize(sio)
        return sio.getvalue().strip()

    def visualize_as_svg(self, config: VisualizationConfig) -> SVGGraphic:
        out = SVGGraphic(config.size, config.size)
        out.draw_rect(0, 0, config.size, config.size, 0, "rgb(255, 255, 255)")

        def _rescale(x):
            return x / self.grid_side_length * config.size

        for city in self.cities:
            out.draw_circle(_rescale(city.x), _rescale(city.y), 2, 0, config.city_color)

        return out
