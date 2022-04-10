import io
import unittest

from instance import Instance
from point import Point
from solution import Solution
from svg import SVGGraphic
from visualize import VisualizationConfig


class TestParseSolution(unittest.TestCase):

    def test_parse_simple(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        solution = Solution.parse("""
# Penalty: 123
3
9 1
3 4
5 6
        """.strip().splitlines(), instance)
        want = Solution(towers=[
            Point(x=9, y=1),
            Point(x=3, y=4),
            Point(x=5, y=6),
        ], instance=instance)
        self.assertEqual(want, solution)

    def test_parse_too_few_towers(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        with self.assertRaises(AssertionError):
            solution = Solution.parse("""
3
9 1
3 4
            """.strip().splitlines(), instance)

    def test_parse_too_many_towers(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        with self.assertRaises(AssertionError):
            solution = Solution.parse("""
3
9 1
3 4
5 6
7 8
            """.strip().splitlines(), instance)

    def test_parse_out_of_bounds(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        with self.assertRaises(AssertionError):
            solution = Solution.parse("""
1
10 0
            """.strip().splitlines(), instance)

    def test_parse_doesnt_cover(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        with self.assertRaises(AssertionError):
            solution = Solution.parse("""
1
0 9
            """.strip().splitlines(), instance)


class TestSolutionValidity(unittest.TestCase):
    def test_invalid_out_of_bounds(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        solution = Solution(
            towers=[Point(x=10, y=0)],
            instance=instance,
        )
        self.assertFalse(solution.valid())

    def test_invalid_doesnt_cover(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        solution = Solution(
            towers=[Point(x=0, y=9)],
            instance=instance,
        )
        self.assertFalse(solution.valid())

    def test_valid(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        solution = Solution(
            towers=[Point(x=9, y=1)],
            instance=instance,
        )
        self.assertTrue(solution.valid())


class TestSolution(unittest.TestCase):
    def setUp(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=0)],
        )
        self.solution = Solution(
            towers=[
                Point(x=0, y=0),
                Point(x=0, y=1),
                Point(x=0, y=2),
                Point(x=5, y=5),
                Point(x=5, y=6),
                Point(x=9, y=9),
            ],
            instance=instance,
        )

    def test_penalty(self):
        self.assertAlmostEqual(1289.52692064, self.solution.penalty())

    def test_serialize_to_string(self):
        self.assertEqual(
            """
6
0 0
0 1
0 2
5 5
5 6
9 9
        """.strip(),
            self.solution.serialize_to_string(),
        )

    def test_serialize(self):
        sio = io.StringIO()
        self.solution.serialize(sio)

        self.assertEqual(
            """
6
0 0
0 1
0 2
5 5
5 6
9 9
        """.strip()
            + "\n",
            sio.getvalue(),
        )

    def test_visualize_as_svg(self):
        reference = """
<svg width="500" height="500" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="500" height="500" stroke="0" fill="rgb(255, 255, 255)" opacity="1" />
    <circle cx="450.0" cy="0.0" r="2" stroke="0" fill="rgb(0, 0, 0)" opacity="1" />
    
    <circle cx="0.0" cy="0.0" r="2" stroke="0" fill="rgb(0, 0, 255)" opacity="1" />
    <circle cx="0.0" cy="0.0" r="50.0" stroke="0" fill="rgb(255, 0, 0)" opacity="0.2" />
    <circle cx="0.0" cy="0.0" r="100.0" stroke="0" fill="rgb(0, 255, 0)" opacity="0.3" />
    
    <circle cx="0.0" cy="50.0" r="2" stroke="0" fill="rgb(0, 0, 255)" opacity="1" />
    <circle cx="0.0" cy="50.0" r="50.0" stroke="0" fill="rgb(255, 0, 0)" opacity="0.2" />
    <circle cx="0.0" cy="50.0" r="100.0" stroke="0" fill="rgb(0, 255, 0)" opacity="0.3" />
    
    <circle cx="0.0" cy="100.0" r="2" stroke="0" fill="rgb(0, 0, 255)" opacity="1" />
    <circle cx="0.0" cy="100.0" r="50.0" stroke="0" fill="rgb(255, 0, 0)" opacity="0.2" />
    <circle cx="0.0" cy="100.0" r="100.0" stroke="0" fill="rgb(0, 255, 0)" opacity="0.3" />
</svg>
"""

        def _remove_whitespace(x):
            # remove all whitespace
            # technically this changes the semantics, but whatever
            return "".join(x.split())

        # shrink size of output
        self.solution.towers = self.solution.towers[:3]

        svg = self.solution.visualize_as_svg(VisualizationConfig(penalty_opacity=0.3))

        self.assertIsInstance(svg, SVGGraphic)

        self.assertEqual(
            _remove_whitespace(reference),
            _remove_whitespace(str(svg)),
        )


if __name__ == "__main__":
    unittest.main()
