__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import main
from src.intcode_computer.tests import TestIntcodeComputer


class TestDay09(TestIntcodeComputer):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        Here are some example programs that use these features:
        -109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99
         takes no input and produces a copy of itself as output.
        -1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
        -104,1125899906842624,99 should output the large number in the middle.
        """

        self._test_output(
            "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99",
            tuple(),
            (109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006,
             101, 0, 99))
        self._test_output("1102,34915192,34915192,7,4,7,99,0", tuple(),
                          tuple([1219070632396864]))
        self._test_output("104,1125899906842624,99", tuple(),
                          tuple([1125899906842624]))

################################################################################

if __name__ == '__main__':
    main()

################################################################################
