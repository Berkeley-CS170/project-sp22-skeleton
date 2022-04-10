from __future__ import annotations

import dataclasses
from typing import ClassVar

from instance import Instance


@dataclasses.dataclass
class Size:
    grid_side_length: int
    coverage_radius: int
    penalty_radius: int
    max_num_cities: int

    SMALL: ClassVar[Size]
    MEDIUM: ClassVar[Size]
    LARGE: ClassVar[Size]

    def instance_has_size(self, instance: Instance):
        return instance.grid_side_length == self.grid_side_length \
            and instance.coverage_radius == self.coverage_radius \
            and instance.penalty_radius == self.penalty_radius \
            and len(instance.cities) <= self.max_num_cities

    def instance(self, cities):
        return Instance(
            grid_side_length=self.grid_side_length,
            coverage_radius=self.coverage_radius,
            penalty_radius=self.penalty_radius,
            cities=cities,
        )


Size.SMALL = Size(
    grid_side_length=30,
    coverage_radius=4,
    penalty_radius=11,
    max_num_cities=40,
)

Size.MEDIUM = Size(
    grid_side_length=50,
    coverage_radius=4,
    penalty_radius=11,
    max_num_cities=50,
)

Size.LARGE = Size(
    grid_side_length=100,
    coverage_radius=4,
    penalty_radius=11,
    max_num_cities=60,
)
