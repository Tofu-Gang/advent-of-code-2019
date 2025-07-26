__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_04.password_range import PasswordRange


class TestDay04(TestCase):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        -111111 meets these criteria (double 11, never decreases).
        -223450 does not meet these criteria (decreasing pair of digits 50).
        -123789 does not meet these criteria (no double).
        """

        password = PasswordRange(100000, 999999)
        self.assertTrue(password.is_password_valid_1(111111))
        self.assertFalse(password.is_password_valid_1(223450))
        self.assertFalse(password.is_password_valid_1(123789))

################################################################################

    def test_puzzle_2(self) -> None:
        """
        -112233 meets these criteria because the digits never decrease and all
         repeated digits are exactly two digits long.
        -123444 no longer meets the criteria (the repeated 44 is part of a
         larger group of 444).
        -111122 meets the criteria (even though 1 is repeated more than twice,
         it still contains a double 22).
        """

        password = PasswordRange(100000, 999999)
        self.assertTrue(password.is_password_valid_2(112233))
        self.assertFalse(password.is_password_valid_2(123444))
        self.assertTrue(password.is_password_valid_2(111122))

################################################################################

if __name__ == '__main__':
    main()

################################################################################
