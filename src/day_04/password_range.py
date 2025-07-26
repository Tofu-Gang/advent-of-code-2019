__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Callable
from itertools import groupby


################################################################################

class PasswordRange:

    def __init__(self, range_start: int, range_end: int):
        """
        The password is from a given range of numbers.
        """

        self._range_start = range_start
        self._range_end = range_end

################################################################################

    def valid_passwords_count(self, validation_function: Callable) -> int:
        """
        :return: number of valid passwords from the given range
        """

        count = 0

        for password in range(self._range_start, self._range_end):
            if validation_function(password):
                count += 1

        return count

################################################################################

    def is_password_valid_1(self, password: int) -> bool:
        """
        A few key facts about the password:
        -It is a six-digit number.
        -The value is within the given range.
        -Two adjacent digits are the same.
        -Going from left to right, the digits never decrease; they only ever
         increase or stay the same.

        :param password: a password candidate
        :return: True if the password is valid (according to puzzle 1), False
        otherwise
        """

        numerals = str(password)

        if len(numerals) != 6:
            # the password is a six-digit number
            return False
        elif password < self._range_start or password > self._range_end:
            # the password value is within the given range
            return False
        elif all(numerals[i] != numerals[i + 1]
                 for i in range(len(numerals) - 1)):
            # two adjacent digits are the same
            return False
        elif any(numerals[i] > numerals[i + 1]
                 for i in range(len(numerals) - 1)):
            # going from left to right, the digits never decrease; they only
            # ever increase or stay the same
            return False
        else:
            # this password is valid
            return True

################################################################################

    def is_password_valid_2(self, password: int) -> bool:
        """
        One more important detail about the password: the two adjacent matching
        digits are not part of a larger group of matching digits.

        :param password: a password candidate
        :return: True if the password is valid (according to puzzle 2), False
        otherwise
        """

        groups = tuple("".join(group) for key, group in groupby(str(password)))
        return (self.is_password_valid_1(password)
                and any(len(group) == 2 for group in groups))

################################################################################
