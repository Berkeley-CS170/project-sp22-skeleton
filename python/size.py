from __future__ import annotations

import dataclasses
from typing import ClassVar

from instance import Instance


@dataclasses.dataclass
class Size:
    grid_side_length: int
    coverage_radius: int
    penalty_radius: int
    min_num_cities: int
    max_num_cities: int

    SMALL: ClassVar[Size]
    MEDIUM: ClassVar[Size]
    LARGE: ClassVar[Size]

    def instance_has_size(self, instance: Instance):
        return instance.grid_side_length == self.grid_side_length \
            and instance.coverage_radius == self.coverage_radius \
            and instance.penalty_radius == self.penalty_radius \
            and self.min_num_cities <= len(instance.cities) <= self.max_num_cities

    def instance(self, cities):
        return Instance(
            grid_side_length=self.grid_side_length,
            coverage_radius=self.coverage_radius,
            penalty_radius=self.penalty_radius,
            cities=cities,
        )


Size.SMALL = Size(
    grid_side_length=30,
    coverage_radius=3,
    penalty_radius=8,
    min_num_cities=15,
    max_num_cities=25,
)

Size.MEDIUM = Size(
    grid_side_length=50,
    coverage_radius=3,
    penalty_radius=10,
    min_num_cities=45,
    max_num_cities=55,
)

Size.LARGE = Size(
    grid_side_length=100,
    coverage_radius=3,
    penalty_radius=14,
    min_num_cities=195,
    max_num_cities=205,
)
