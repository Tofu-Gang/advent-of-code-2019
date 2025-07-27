__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase
from src.intcode_computer.intcode_computer import IntcodeComputer


################################################################################

class TestIntcodeComputer(TestCase):

    def _test_program(self, program: str, result_value: int,
                      address: int | None=None,
                      input_value: int | None=None) -> None:
        """
        Test an Intcode program by running it and then comparing a value from
        a specified address with an expected one; if no address is provided, the
        last value from the output is used for the comparison. Intcode computer
        can be provided with an input value.

        :param program: an Intcode program
        :param result_value: an expected value to test against
        :param address: an address of the test value
        :param input_value: optional input value
        """

        computer = IntcodeComputer()
        computer.load_program(program)
        if input_value is not None:
            computer.set_input(input_value)
        computer.start()
        computer.join()

        if address is not None:
            self.assertEqual(computer.get_value(address), result_value)
        else:
            self.assertEqual(computer.output[-1], result_value)

################################################################################
