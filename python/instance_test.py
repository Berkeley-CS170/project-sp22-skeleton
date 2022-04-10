import io
import unittest

from instance import Instance
from point import Point
from svg import SVGGraphic
from visualize import VisualizationConfig


class TestParseInstance(unittest.TestCase):

    def test_simple(self):
        lines = """
5
10
1
2
5 9
2 2
1 1
2 3
0 1
        """.strip().splitlines()

        want = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[
                Point(x=5, y=9),
                Point(x=2, y=2),
                Point(x=1, y=1),
                Point(x=2, y=3),
                Point(x=0, y=1),
            ]
        )

        self.assertEqual(want, Instance.parse(lines))

    def test_too_few_parameters(self):
        lines = """
5
10
1
        """.strip().splitlines()

        with self.assertRaises(StopIteration):
            Instance.parse(lines)

    def test_point_oob(self):
        lines = """
1
10
1
2
1 10
        """.strip().splitlines()

        with self.assertRaises(AssertionError):
            Instance.parse(lines)

    def test_too_few_points(self):
        lines = """
5
10
1
2
1 2
3 4
        """.strip().splitlines()

        with self.assertRaises(AssertionError):
            Instance.parse(lines)

    def test_too_many_points(self):
        lines = """
5
10
1
2
1 2
3 4
5 6
7 8
9 0
1 5
        """.strip().splitlines()

        with self.assertRaises(AssertionError):
            Instance.parse(lines)

    def test_duplicate_points(self):
        lines = """
2
10
1
2
1 2
1 2
        """.strip().splitlines()

        with self.assertRaises(AssertionError):
            Instance.parse(lines)


class TestInstance(unittest.TestCase):

    def test_invalid_oob(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=10, y=0)],
        )
        self.assertFalse(instance.valid())

    def test_invalid_oob_negative(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[Point(x=9, y=-1)],
        )
        self.assertFalse(instance.valid())

    def test_invalid_duplicate(self):
        instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[
                Point(x=1, y=0),
                Point(x=1, y=0),
            ],
        )
        self.assertFalse(instance.valid())


class TestInstanceSerialization(unittest.TestCase):
    def setUp(self):
        self.instance = Instance(
            grid_side_length=10,
            coverage_radius=1,
            penalty_radius=2,
            cities=[
                Point(x=1, y=0),
                Point(x=1, y=2),
            ],
        )

    def test_serialize(self):
        sio = io.StringIO()
        self.instance.serialize(sio)
        self.assertEqual(
            """
2
10
1
2
1 0
1 2
        """.strip() + "\n", sio.getvalue())

    def test_serialize_to_string(self):
        self.assertEqual(
            """
2
10
1
2
1 0
1 2
        """.strip(),
            self.instance.serialize_to_string(),
        )

    def test_visualize_as_svg(self):
        reference = """
<svg width="500" height="500" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="500" height="500" stroke="0" fill="rgb(255, 255, 255)" opacity="1" />
    <circle cx="50.0" cy="0.0" r="2" stroke="0" fill="rgb(0, 0, 0)" opacity="1" />
    <circle cx="50.0" cy="100.0" r="2" stroke="0" fill="rgb(0, 0, 0)" opacity="1" />
</svg>"""

        def _remove_whitespace(x):
            # remove all whitespace
            # technically this changes the semantics, but whatever
            return "".join(x.split())

        svg = self.instance.visualize_as_svg(VisualizationConfig())

        self.assertIsInstance(svg, SVGGraphic)

        self.assertEqual(
            _remove_whitespace(reference),
            _remove_whitespace(str(svg)),
        )


if __name__ == "__main__":
    unittest.main()
