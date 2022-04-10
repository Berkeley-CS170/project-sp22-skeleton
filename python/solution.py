from __future__ import annotations

import dataclasses
import io
import math
from typing import List, Iterable

from point import Point
from instance import Instance


@dataclasses.dataclass
class Solution:
    towers: List[Point]
    instance: Instance

    def valid(self):
        for tower in self.towers:
            if not 0 <= tower.x < self.instance.grid_side_length:
                return False
            if not 0 <= tower.y < self.instance.grid_side_length:
                return False

        for city in self.instance.cities:
            for tower in self.towers:
                if Point.distance(city, tower) <= self.instance.coverage_radius:
                    break
            else:
                return False

        return len(set(self.towers)) == len(self.towers)

    def deduplicate(self):
        # Use dict to preserve tower order.
        self.towers = list({tower: () for tower in self.towers}.keys())

    @staticmethod
    def parse(lines: Iterable[str], instance: Instance):
        lines = iter(lines)
        num_towers_s = next(lines, None)
        assert num_towers_s is not None
        num_towers = int(num_towers_s)

        towers = []
        for line in lines:
            towers.append(Point.parse(line))
        assert num_towers == len(towers)

        sol = Solution(towers=towers, instance=instance)
        assert sol.valid()
        return sol

    def serialize(self, out):
        print(len(self.towers), file=out)
        for tower in self.towers:
            print(tower.x, tower.y, file=out)

    def serialize_to_string(self):
        sio = io.StringIO()
        self.serialize(sio)
        return sio.getvalue().strip()

    def penalty(self):
        penalty = 0
        for fidx, first in enumerate(self.towers):
            num_overlaps = 0
            for sidx, second in enumerate(self.towers):
                if fidx == sidx:
                    continue
                if Point.distance(first, second) <= self.instance.penalty_radius:
                    num_overlaps += 1
            penalty += 170 * math.exp(0.17 * num_overlaps)
        return penalty
