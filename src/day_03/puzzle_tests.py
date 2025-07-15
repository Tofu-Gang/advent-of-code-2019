__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import TestCase, main
from src.day_03.wire import Wire


class TestDay03(TestCase):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        Here are a few examples:
        -R8,U5,L5,D3
        -U7,R6,D4,L4 = distance 6
        -R75,D30,R83,U83,L12,D49,R71,U7,L72
        -U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
        -R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
        -U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
        """

        self.assertEqual(
            Wire("R8,U5,L5,D3").closest_intersection_distance(
                Wire("U7,R6,D4,L4")), 6)
        self.assertEqual(
            Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
            .closest_intersection_distance(
                Wire("U62,R66,U55,R34,D71,R55,D58,R83")), 159)
        self.assertEqual(
            Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
            .closest_intersection_distance(
                Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")), 135)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        Here are the best steps for the extra examples from above:
        -R8,U5,L5,D3
        -U7,R6,D4,L4 = 30 steps
        -R75,D30,R83,U83,L12,D49,R71,U7,L72
        -U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
        -R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
        -U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
        """

        self.assertEqual(
            Wire("R8,U5,L5,D3").least_intersection_delay(
                Wire("U7,R6,D4,L4")), 30)
        self.assertEqual(
            Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72").least_intersection_delay(
                Wire("U62,R66,U55,R34,D71,R55,D58,R83")), 610)
        self.assertEqual(
            Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
            .least_intersection_delay(
                Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")), 410)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
