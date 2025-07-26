__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple
from src.day_06.space_object import SpaceObject


################################################################################

class CosmicMap:
    DELIMITER = ")"
    CENTER_OF_MASS = "COM"
    YOU = "YOU"
    SANTA = "SAN"

################################################################################

    def __init__(self, lines: Tuple[str]):
        """
        Associate space objects with its names in a dict. Link each space object
        to its orbit center.
        """

        # create all space objects
        self._cosmic_map = {
            orbiter_name: SpaceObject(orbiter_name)
            for orbiter_name in map(
                lambda line: line.split(self.DELIMITER)[1],
                lines)
        }
        self._cosmic_map[self.CENTER_OF_MASS] = SpaceObject(self.CENTER_OF_MASS)

        # link each space object to its orbit center
        for line in lines:
            try:
                orbit_center_name, orbiter_name = line.split(self.DELIMITER)
                orbiter = self._cosmic_map[orbiter_name]
                orbit_center = self._cosmic_map[orbit_center_name]
                orbiter.set_orbit_center(orbit_center)
            except KeyError:
                # COM does not orbit anything
                pass

################################################################################

    @property
    def orbit_count_checksum(self) -> int:
        """
        :return: the total number of direct and indirect orbits in the map data
        """

        return sum(self._get_orbits_count(name)
                   for name in self._cosmic_map)

################################################################################

    @property
    def santa_transfers_count(self) -> int:
        """
        :return: the minimum number of orbital transfers required to move from
        the object YOU are orbiting to the object SAN is orbiting
        """

        you = self._cosmic_map[self.YOU]
        you.set_distance(0)
        current = you

        while current.name != self.SANTA:
            # current orbiter is visited, never process it again
            current.set_visited()
            neighbors = self._get_unvisited_neighbors(current.name)

            # set the distances
            for neighbor in neighbors:
                neighbor.set_distance(
                    min(current.distance + 1, neighbor.distance))
            try:
                # get the location with the least tentative distance
                current = sorted(
                    [location
                     for location in self._cosmic_map.values()
                     if not location.is_visited],
                    key=lambda location: location.distance)[0]
            except IndexError:
                # no unvisited locations left
                break

        # -2 because between the objects they are orbiting - not between YOU and
        # SAN
        return current.distance - 2

################################################################################

    def _get_orbits_count(self, orbiter_name: str) -> int:
        """
        :param orbiter_name: space object name
        :return: number of direct and indirect orbits of the specified space
        object
        """

        count = 0
        while True:
            try:
                orbiter_name = self._cosmic_map[orbiter_name].orbit_center.name
                count += 1
            except AttributeError:
                # COM reached; COM does not orbit anything
                break
        return count

################################################################################

    def _get_unvisited_neighbors(
            self, current_location_name: str) -> Tuple[SpaceObject]:
        """
        :param current_location_name: current space object name
        :return: tuple of all unvisited neighbor space objects (space object the
        current one orbits around or space object that orbit around the current
        one)
        """

        current_location = self._cosmic_map[current_location_name]
        return tuple(filter(
            lambda location:
            not location.is_visited
            and (location.orbit_center is current_location
                 or location is current_location.orbit_center),
            self._cosmic_map.values()))

################################################################################
