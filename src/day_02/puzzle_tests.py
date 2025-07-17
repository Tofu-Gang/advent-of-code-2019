__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import main
from src.intcode_computer.tests import TestIntcodeComputer


class TestDay02(TestIntcodeComputer):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        For example, suppose you have the following program:
        1,9,10,3,2,3,11,0,99,30,40,50

        For the purposes of illustration, here is the same program split into
        multiple lines:
        1,9,10,3,
        2,3,11,0,
        99,
        30,40,50

        The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3.
        Together, they represent the first opcode (1, addition), the positions
        of the two inputs (9 and 10), and the position of the output (3). To
        handle this opcode, you first need to get the values at the input
        positions: position 9 contains 30, and position 10 contains 40. Add
        these numbers together to get 70. Then, store this value at the output
        position; here, the output position (3) is at position 3, so it
        overwrites itself. Afterward, the program looks like this:
        1,9,10,70,
        2,3,11,0,
        99,
        30,40,50

        Step forward 4 positions to reach the next opcode, 2. This opcode works
        just like the previous, but it multiplies instead of adding. The inputs
        are at positions 3 and 11; these positions contain 70 and 50
        respectively. Multiplying these produces 3500; this is stored at
        position 0:
        3500,9,10,70,
        2,3,11,0,
        99,
        30,40,50

        Stepping forward 4 more positions arrives at opcode 99, halting the
        program.

        Here are the initial and final states of a few more small programs:
        1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
        2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
        2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
        1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
        """

        self._test_program("1,9,10,3,2,3,11,0,99,30,40,50", 3500, 0)
        self._test_program("1,9,10,3,2,3,11,0,99,30,40,50", 70, 3)
        self._test_program("1,0,0,0,99", 2, 0)
        self._test_program("2,3,0,3,99",6, 3)
        self._test_program("2,4,4,5,99,0", 9801, 5)
        self._test_program("1,1,1,4,99,5,6,0,99", 30, 0)
        self._test_program("1,1,1,4,99,5,6,0,99", 2, 4)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
