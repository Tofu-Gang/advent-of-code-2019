__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from unittest import main, TestCase
from src.day_06.cosmic_map import CosmicMap


class TestDay06(TestCase):

################################################################################

    def test_puzzle_1(self) -> None:
        """
        For example, suppose you have the following map:
        COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L

        Visually, the above map of orbits looks like this:
                G - H       J - K - L
               /           /
        COM - B - C - D - E - F
                       \
                        I

        In this visual representation, when two objects are connected by a line,
        the one on the right directly orbits the one on the left.

        Here, we can count the total number of orbits as follows:
        -D directly orbits C and indirectly orbits B and COM, a total of 3
         orbits.
        -L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a
         total of 7 orbits.
        -COM orbits nothing.

        The total number of direct and indirect orbits in this example is 42.
        """

        lines = tuple(map(
            str.strip,
            "COM)B\n"
            "B)C\n"
            "C)D\n"
            "D)E\n"
            "E)F\n"
            "B)G\n"
            "G)H\n"
            "D)I\n"
            "E)J\n"
            "J)K\n"
            "K)L".split("\n")))
        orbits_map = CosmicMap(lines)
        self.assertEqual(orbits_map.orbit_count_checksum, 42)

################################################################################

    def test_puzzle_2(self) -> None:
        """
        For example, suppose you have the following map:
        COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L
        K)YOU
        I)SAN

        Visually, the above map of orbits looks like this:
                                  YOU
                                 /
                G - H       J - K - L
               /           /
        COM - B - C - D - E - F
                       \
                        I - SAN

        In this example, YOU are in orbit around K, and SAN is in orbit around
        I. To move from K to I, a minimum of 4 orbital transfers are required:
        -K to J
        -J to E
        -E to D
        -D to I

        Afterward, the map of orbits looks like this:
                G - H       J - K - L
               /           /
        COM - B - C - D - E - F
                       \
                        I - SAN
                         \
                          YOU
        """

        lines = tuple(map(
            str.strip,
            "COM)B\n"
            "B)C\n"
            "C)D\n"
            "D)E\n"
            "E)F\n"
            "B)G\n"
            "G)H\n"
            "D)I\n"
            "E)J\n"
            "J)K\n"
            "K)L\n"
            "K)YOU\n"
            "I)SAN".split("\n")))
        orbits_map = CosmicMap(lines)
        self.assertEqual(orbits_map.santa_transfers_count, 4)

################################################################################

if __name__ == '__main__':
    main()

################################################################################
