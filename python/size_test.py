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
            min_num_cities=1,
            max_num_cities=2,
        )
        instance = Instance(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            cities=[Point(x=1, y=2)],
        )

        self.assertTrue(size.instance_has_size(instance))

    def test_different_grid_side_length(self):
        size = Size(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            min_num_cities=1,
            max_num_cities=2
        )
        instance = Instance(
            grid_side_length=11,
            coverage_radius=2,
            penalty_radius=1,
            cities=[],
        )

        self.assertFalse(size.instance_has_size(instance))

    def test_different_penalty(self):
        size = Size(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            min_num_cities=1,
            max_num_cities=2
        )
        different_penalty = Instance(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=0,
            cities=[],
        )

        self.assertFalse(size.instance_has_size(different_penalty))

    def test_different_coverage(self):
        size = Size(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            min_num_cities=1,
            max_num_cities=2
        )
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=1,
            cities=[],
        )

        self.assertFalse(size.instance_has_size(instance))

    def test_too_many_cities(self):
        size = Size(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            min_num_cities=1,
            max_num_cities=2
        )
        instance = Instance(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            cities=[
                Point(x=1, y=2),
                Point(x=2, y=2),
                Point(x=3, y=2),
            ],
        )

        self.assertFalse(size.instance_has_size(instance))

    def test_too_few_cities(self):
        size = Size(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            min_num_cities=1,
            max_num_cities=2
        )
        instance = Instance(
            grid_side_length=10,
            coverage_radius=2,
            penalty_radius=1,
            cities=[],
        )

        self.assertFalse(size.instance_has_size(instance))


if __name__ == "__main__":
    unittest.main()
