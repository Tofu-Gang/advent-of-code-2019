__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import main
from src.intcode_computer.tests import TestIntcodeComputer


class TestDay02(TestIntcodeComputer):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        -The program 3,0,4,0,99 outputs whatever it gets as input, then halts.
        -The program 1002,4,3,4,33 multiplies 33 by 3 and stores the result on
         the address 4, creating opcode 99 which halts the program.
        -Integers can be negative: 1101,100,-1,4,0 finds 100 + -1 (99), stores
         the result in position 4, again creating opcode 99 which halts the
         program.
        """

        self._test_output("3,0,4,0,99", tuple([333]), tuple([333]))
        self._test_address_value(
            "1002,4,3,4,33", tuple(), 4, 99)
        self._test_address_value(
            "1101,100,-1,4,0", tuple(), 4, 99)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For example, here are several programs that take one input, compare it
        to the value 8, and then produce one output:
        -3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the
         input is equal to 8; output 1 (if it is) or 0 (if it is not).
        -3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the
         input is less than 8; output 1 (if it is) or 0 (if it is not).
        -3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the
         input is equal to 8; output 1 (if it is) or 0 (if it is not).
        -3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the
         input is less than 8; output 1 (if it is) or 0 (if it is not).

        Here are some jump tests that take an input, then output 0 if the input
        was zero or 1 if the input was non-zero:
        -3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
        -3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)

        Here's a larger example:
        -3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
         1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
         999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99

        The above example program uses an input instruction to ask for a single
        number. The program will then output 999 if the input value is below 8,
        output 1000 if the input value is equal to 8, or output 1001 if the
        input value is greater than 8.
        """

        self._test_output(
            "3,9,8,9,10,9,4,9,99,-1,8", tuple([8]), tuple([1]))
        self._test_output(
            "3,9,8,9,10,9,4,9,99,-1,8", tuple([5]), tuple([0]))
        self._test_output(
            "3,9,7,9,10,9,4,9,99,-1,8", tuple([5]), tuple([1]))
        self._test_output(
            "3,9,7,9,10,9,4,9,99,-1,8", tuple([8]), tuple([0]))
        self._test_output(
            "3,3,1108,-1,8,3,4,3,99", tuple([8]), tuple([1]))
        self._test_output(
            "3,3,1108,-1,8,3,4,3,99", tuple([5]), tuple([0]))
        self._test_output(
            "3,3,1107,-1,8,3,4,3,99", tuple([5]), tuple([1]))
        self._test_output(
            "3,3,1107,-1,8,3,4,3,99", tuple([8]), tuple([0]))

        self._test_output(
            "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9",
            tuple([0]), tuple([0]))
        self._test_output(
            "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9",
            tuple([8]), tuple([1]))
        self._test_output(
            "3,3,1105,-1,9,1101,0,0,12,4,12,99,1",
            tuple([0]), tuple([0]))
        self._test_output(
            "3,3,1105,-1,9,1101,0,0,12,4,12,99,1",
            tuple([8]), tuple([1]))

        self._test_output(
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,"
            "0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,"
            "1000,1,20,4,20,1105,1,46,98,99", tuple([5]), tuple([999]))
        self._test_output(
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,"
            "0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,"
            "1000,1,20,4,20,1105,1,46,98,99", tuple([8]), tuple([1000]))
        self._test_output(
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,"
            "0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,"
            "1000,1,20,4,20,1105,1,46,98,99", tuple([14]), tuple([1001]))

################################################################################

if __name__ == '__main__':
    main()

################################################################################
