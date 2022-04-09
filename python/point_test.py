import unittest

from point import Point
from distance import Distance

class TestParsePoint(unittest.TestCase):

    def test_simple(self):
        line = "2 3"
        want = Point(x=2, y=3)
        self.assertEqual(want, Point.parse(line))

    def test_too_few_coords(self):
        line = "2"
        with self.assertRaises(AssertionError):
            Point.parse(line)

    def test_too_many_coords(self):
        line = "2 3 4"
        with self.assertRaises(AssertionError):
            Point.parse(line)

    def test_replace_x(self):
        point = Point(1, 2)
        want = Point(3, 2)
        self.assertEqual(want, point.replace(x=3))

    def test_distance(self):
        first = Point(1, 2)
        second = Point(3, 3)
        want = Distance(5)
        self.assertEqual(want, Point.distance(first, second))

if __name__ == '__main__':
    unittest.main()
