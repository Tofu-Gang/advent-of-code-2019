__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Self
from sys import maxsize


################################################################################

class SpaceObject:

    def __init__(self, name: str):
        """
        Space is identified by its unique name. It is created as unvisited,
        orbiting nothing and unset distance from the object YOU are orbiting.
        """

        self._name = name
        self._orbit_center = None
        self._visited = False
        self._distance = maxsize

################################################################################

    @property
    def name(self) -> str:
        """
        :return: space object name
        """

        return self._name

################################################################################

    @property
    def orbit_center(self) -> Self | None:
        """
        :return: space object this one orbits around or None (in case of freshly
        created space object or COM)
        """

        return self._orbit_center

################################################################################

    @property
    def is_visited(self) -> bool:
        """
        :return: True if this space object has been visited, False otherwise
        """

        return self._visited

################################################################################

    @property
    def distance(self) -> int:
        """
        :return: distance to the space object YOU are orbiting
        """

        return self._distance

################################################################################

    def set_orbit_center(self, orbit_center: Self) -> None:
        """
        Set the space object this one orbits around.
        :param orbit_center: this space object orbit center
        """

        self._orbit_center = orbit_center

################################################################################

    def set_visited(self) -> None:
        """
        Set this space object as visited.
        """

        self._visited = True

################################################################################

    def set_distance(self, distance: int) -> None:
        """
        Set the distance from the space object YOU are orbiting.

        :param distance: distance from the space object YOU are orbiting
        """

        self._distance = distance

################################################################################
