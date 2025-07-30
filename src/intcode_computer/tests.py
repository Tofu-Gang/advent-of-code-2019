__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple
from unittest import TestCase
from src.intcode_computer.intcode_computer import IntcodeComputer


################################################################################

class TestIntcodeComputer(TestCase):

    def _init_computer(
            self, program: str, input_values: Tuple[int]) -> IntcodeComputer:
        """
        Init an Intcode Computer and run the specified program. Return the
        computer after the program finished running.

        :param program: an Intcode program
        :param input_values: input values
        :return: the computer after the program finished running
        """

        computer = IntcodeComputer()
        computer.load_program(program)
        for value in input_values:
            computer.set_input(value)
        computer.start()
        computer.join()
        return computer

################################################################################

    def _test_output(
            self, program: str, input_values: Tuple[int],
            result: Tuple[int]) -> None:
        """
        Init an Intcode Computer and run the specified program. Compare its
        output with an expected result.

        :param program: an Intcode program
        :param input_values: input values
        :param result: an expected output
        """

        computer = self._init_computer(program, input_values)
        self.assertEqual(computer.output, result)

################################################################################

    def _test_address_value(
            self, program: str, input_values: Tuple[int], address: int,
            result: int) -> None:
        """
        Init an Intcode Computer and run the specified program. Compare a value
        on a specified address in the memory with an expected result.

        :param program: an Intcode program
        :param input_values: input values
        :param address: a memory address
        :param result: an expected value
        """

        computer = self._init_computer(program, input_values)
        self.assertEqual(computer.get_value(address), result)

################################################################################
