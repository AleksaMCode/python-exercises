import unittest

from problem_7.exceptions import DenominatorZeroException
from problem_7.problem7 import Fraction
from parameterized import parameterized


class TestFraction(unittest.TestCase):
    fractions_addition = [
        [Fraction(37, 13), Fraction(18, 15), Fraction(789, 195)],
        [Fraction(10, 2), Fraction(8, 4), Fraction(28, 4)],
        [Fraction(1, 1), Fraction(15, 32), Fraction(47, 32)],
    ]

    fractions_multiplication = [
        [Fraction(37, 13), Fraction(18, 15), Fraction(666, 195)],
        [Fraction(10, 2), Fraction(8, 4), Fraction(80, 8)],
        [Fraction(1, 1), Fraction(15, 32), Fraction(15, 32)],
    ]

    def test_fraction_reduction(self):
        fraction = Fraction(10, 4)
        reduced_fraction = fraction.get_reduced()
        self.assertEqual(5, reduced_fraction.numerator)
        self.assertEqual(2, reduced_fraction.denominator)

    @parameterized.expand([
        [87, 33, 3],
        [26, 1128, 2],
        [31, 169, 1],
        [24, 36, 12],
    ])
    def test_gcd(self, first, second, result):
        self.assertEqual(result, Fraction.get_gcd(first, second))

    @parameterized.expand(fractions_addition)
    def test_fraction_addition(self, frac1, frac2, expected_value):
        expected_value = expected_value.get_reduced()
        frac_sum = frac1 + frac2
        self.assertEqual(expected_value.numerator, frac_sum.numerator)
        self.assertEqual(expected_value.denominator, frac_sum.denominator)

    @parameterized.expand(fractions_multiplication)
    def test_fraction_multiplication(self, frac1, frac2, expected_value):
        expected_value = expected_value.get_reduced()
        frac_mul = frac1 * frac2
        self.assertEqual(expected_value.numerator, frac_mul.numerator)
        self.assertEqual(expected_value.denominator, frac_mul.denominator)

    def test_denominator_zero_exception(self):
        with self.assertRaises(DenominatorZeroException):
            fraction = Fraction(5, 0)


if __name__ == '__main__':
    unittest.main()
