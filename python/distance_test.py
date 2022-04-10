from __future__ import annotations

import unittest

from distance import Distance, DoNotImplement


class TestDistance(unittest.TestCase):

    def test_negative_construct(self):
        with self.assertRaises(AssertionError):
            Distance(-10)

    def test_str(self):
        dist = Distance(3)
        self.assertEqual("sqrt(3)", str(dist))

    def test_repr(self):
        dist = Distance(3)
        self.assertEqual("Distance(3)", repr(dist))

    def test_eq(self):
        self.assertEqual(Distance(3), Distance(3))
        self.assertNotEqual(Distance(4), Distance(3))

    def test_lt(self):
        self.assertLess(Distance(2), Distance(3))

    def test_le(self):
        self.assertLessEqual(Distance(2), Distance(3))
        self.assertLessEqual(Distance(3), Distance(3))

    def test_gt(self):
        self.assertGreater(Distance(4), Distance(3))

    def test_ge(self):
        self.assertGreaterEqual(Distance(4), Distance(3))
        self.assertGreaterEqual(Distance(3), Distance(3))

    def test_eq_num(self):
        self.assertEqual(Distance(9), 3)
        self.assertNotEqual(Distance(9), 4)

    def test_lt_num(self):
        self.assertLess(Distance(9), 4)
        self.assertLess(Distance(9), -1)

    def test_le_num(self):
        self.assertLessEqual(Distance(9), 3)
        self.assertLessEqual(Distance(9), 4)
        self.assertLessEqual(Distance(9), -1)

    def test_gt_num(self):
        self.assertGreater(Distance(9), 2)

    def test_ge_num(self):
        self.assertGreaterEqual(Distance(9), 2)
        self.assertGreaterEqual(Distance(9), 3)

    def test_eq_complex(self):
        self.assertEqual(Distance(1), complex(1, 0))
        self.assertNotEqual(Distance(1), complex(2, 0))
        self.assertNotEqual(Distance(1), complex(1, 1))

    def test_lt_complex(self):
        self.assertLess(Distance(9), complex(4, 0))
        with self.assertRaises(ValueError):
            Distance(9) < complex(4, 1)

    def test_le_complex(self):
        self.assertLessEqual(Distance(9), complex(3, 0))
        self.assertLessEqual(Distance(9), complex(4, 0))
        with self.assertRaises(ValueError):
            Distance(9) <= complex(3, 1)
            Distance(9) <= complex(4, 1)

    def test_gt_complex(self):
        self.assertGreater(Distance(9), complex(2, 0))
        with self.assertRaises(ValueError):
            Distance(9) > complex(2, 1)

    def test_ge_complex(self):
        self.assertGreaterEqual(Distance(9), complex(2, 0))
        self.assertGreaterEqual(Distance(9), complex(3, 0))
        with self.assertRaises(ValueError):
            Distance(9) >= complex(2, 1)
            Distance(9) >= complex(3, 1)

    def test_power_two(self):
        self.assertEqual(10, Distance(10) ** 2)

    def test_power_not_two(self):
        with self.assertRaises(ValueError):
            Distance(10) ** 3

    def test_add(self):
        with self.assertRaises(DoNotImplement):
            Distance(10) + Distance(10)

    def test_sub(self):
        with self.assertRaises(DoNotImplement):
            Distance(10) - Distance(10)

    def test_mul(self):
        with self.assertRaises(DoNotImplement):
            Distance(10) * Distance(10)

    def test_truediv(self):
        with self.assertRaises(DoNotImplement):
            Distance(10) / Distance(10)

    def test_floordiv(self):
        with self.assertRaises(DoNotImplement):
            Distance(10) // Distance(10)

    def test_divmod(self):
        with self.assertRaises(DoNotImplement):
            divmod(Distance(10), Distance(10))

    def test_neg(self):
        with self.assertRaises(DoNotImplement):
            -Distance(10)


if __name__ == "__main__":
    unittest.main()
