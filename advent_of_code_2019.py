__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
Santa has become stranded at the edge of the Solar System while delivering 
presents to other planets! To accurately calculate his position in space, safely 
align his warp drive, and return to Earth in time to save Christmas, he needs 
you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day 
in the Advent calendar; the second puzzle is unlocked when you complete the 
first. Each puzzle grants one star. Good luck!
"""

from unittest import TestCase, main
from src.day_01.puzzle import (puzzle_01 as day_01_puzzle_01,
                               puzzle_02 as day_01_puzzle_02)
from src.day_02.puzzle import (puzzle_01 as day_02_puzzle_01,
                               puzzle_02 as day_02_puzzle_02)
from src.day_03.puzzle import (puzzle_01 as day_03_puzzle_01,
                               puzzle_02 as day_03_puzzle_02)


################################################################################

class TestAdventOfCode2019(TestCase):

    def test_day_01(self) -> None:
        self.assertEqual(day_01_puzzle_01(), 3235550)
        self.assertEqual(day_01_puzzle_02(), 4850462)

    def test_day_02(self) -> None:
        self.assertEqual(day_02_puzzle_01(), 3654868)
        self.assertEqual(day_02_puzzle_02(), 7014)

    def test_day_03(self) -> None:
        self.assertEqual(day_03_puzzle_01(), 870)
        self.assertEqual(day_03_puzzle_02(), 13698)

################################################################################

if __name__ == "__main__":
    """
    Runs specified puzzles.
    """

    main()

################################################################################
