# This is used for Postponed Evaluation of Annotations.
# https://stackoverflow.com/questions/15853469/putting-current-class-as-return-type-annotation
from __future__ import annotations
import copy

from problem_7.exceptions import DenominatorZeroException


class Fraction:
    """
    Implementation of mathematical fractions. Problem of limited precision when numbers such as 1/12, 5/4, 9/35, etc.
    are represented in a floating point variable type is solved with this class.
    """

    def __init__(self, numerator: int, denominator: int):

        if denominator == 0:
            raise DenominatorZeroException("Division with zero isn't permitted.")

        self.numerator: int = numerator
        self.denominator: int = denominator

        # Move the negative value up to the numerator if the denominator is negative
        if denominator < 0:
            numerator *= -1
            denominator *= -1

    def __str__(self) -> str:
        red = self.get_reduced()
        return f"{self.numerator}/{self.denominator}={int(red.numerator)}/{int(red.denominator)}"

    def _to_denominator(self, target_denominator: int) -> Fraction:
        """
        Change the dominator value of the fraction to the target value.
        :param target_denominator: Target value of the dominator
        :return: Fraction with a new dominator value
        """
        modified_fraction = copy.deepcopy(self)

        # Can't reduce to a smaller denominator or a target denominator must be a factor of the current denominator
        if target_denominator < self.denominator or target_denominator % self.denominator != 0:
            return modified_fraction

        if self.denominator != target_denominator:
            factor = target_denominator / self.denominator
            modified_fraction.denominator = target_denominator
            modified_fraction.numerator *= factor

        return modified_fraction

    @staticmethod
    def get_gcd(denominator1: int, denominator2: int) -> int:
        """
        Gets the greatest common denominator between two integers.
        :param denominator1: First integer
        :param denominator2: Second integer
        :return: GCD for two integers
        """
        den1 = abs(denominator1)
        den2 = abs(denominator2)

        while den1 != 0 and den2 != 0:
            if den1 > den2:
                den1 %= den2
            else:
                den2 %= den1

        if den1 == 0:
            return den2
        else:
            return den1

    @staticmethod
    def get_lcd(denominator1: int, denominator2: int) -> int:
        """
        Gets the Least Common Denominator between two integers.
        :param denominator1: First integer
        :param denominator2: Second integer
        :return: LCD for two integers
        """
        denominator1 = abs(denominator1)
        denominator2 = abs(denominator2)

        return int(denominator1 * denominator2 / Fraction.get_gcd(denominator1, denominator2))

    def get_reduced(self) -> Fraction:
        """
        Reduce the fraction to its lowest terms.
        :return: Reduced fraction
        """
        modified_fraction = copy.deepcopy(self)

        gcd = abs(Fraction.get_gcd(modified_fraction.numerator, modified_fraction.denominator))

        while abs(gcd) != 1:
            modified_fraction.numerator /= gcd
            modified_fraction.denominator /= gcd
            gcd = abs(Fraction.get_gcd(modified_fraction.numerator, modified_fraction.denominator))

        if modified_fraction.denominator < 0:
            modified_fraction.numerator = -self.numerator
            modified_fraction.denominator = -self.denominator

        return modified_fraction

    def __add__(self, other: Fraction) -> Fraction:
        lcd = 0

        if other is None:
            return self
        else:
            lcd = Fraction.get_lcd(self.denominator, other.denominator)

        self = self._to_denominator(lcd)
        other = other._to_denominator(lcd)

        return Fraction(self.numerator + other.numerator, lcd).get_reduced()

    def __mul__(self, other: Fraction) -> Fraction:
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator).get_reduced()
