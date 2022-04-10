import unittest

from instance import Instance
from point import Point
from size import Size


class TestSize(unittest.TestCase):

    def test_same_size(self):
        size = Size(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            max_num_cities=2
        )
        instance = Instance(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            cities=[Point(x=1, y=2)],
        )

        self.assertTrue(size.instance_has_size(instance))

    def test_different_size(self):
        size = Size(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            max_num_cities=2
        )
        different_penalty = Instance(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=0,
            cities=[],
        )
        different_coverage = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=1,
            cities=[],
        )
        different_grid_side_length = Instance(
            grid_side_length=9,
            coverage_radius=2,
            penalty_radius=1,
            cities=[],
        )
        too_many_cities = Instance(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            cities=[
                Point(x=1, y=2),
                Point(x=2, y=2),
                Point(x=3, y=2),
            ],
        )

        self.assertFalse(size.instance_has_size(different_penalty))
        self.assertFalse(size.instance_has_size(different_coverage))
        self.assertFalse(size.instance_has_size(different_grid_side_length))
        self.assertFalse(size.instance_has_size(too_many_cities))


if __name__ == "__main__":
    unittest.main()
