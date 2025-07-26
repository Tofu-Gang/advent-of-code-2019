__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from src.day_03.point import Point
from src.day_03.vector import Vector
from typing import Tuple, Self, Any


################################################################################

class Wire:
    DENOMINATOR = ","

################################################################################

    def __init__(self, path: str):
        """
        A wire consists of a list of vectors starting in the central port
        (0, 0).
        """

        self._vectors = []
        point_from = Point(0, 0)

        for instruction in path.strip().split(self.DENOMINATOR):
            direction = instruction[0]
            distance = int(instruction[1:])
            vector = Vector(direction, distance, point_from)
            self._vectors.append(vector)
            point_from = vector.point_to

################################################################################

    @property
    def vectors(self) -> Tuple[Any, ...]:
        """
        :return: wire vectors
        """

        return tuple(self._vectors)

################################################################################

    def closest_intersection_distance(self, other: Self) -> int:
        """
        :param other: other wire
        :return: Manhattan distance to the closest wires intersection (puzzle 1)
        """

        return min(abs(intersection.x) + abs(intersection.y)
                   for intersection in self._intersections(other))

################################################################################

    def least_intersection_delay(self, other: Self) -> int:
        """
        :param other: other wire
        :return: least number of steps an intersection with other wire can be
        reached (sum of number of steps taken on both wires) (puzzle 2)
        """

        return min(self.steps_to_point(intersection)
                   + other.steps_to_point(intersection)
                   for intersection in self._intersections(other))

################################################################################

    def steps_to_point(self, point: Point) -> int | None:
        """
        :param point: a point
        :return: a number of steps the point can be reached on this wire or None
        if the point is outside of this wire
        """

        steps = 0
        for vector in self._vectors:
            if vector.contains_point(point):

                if vector.is_horizontal:
                    steps += abs(point.x - vector.point_from.x)
                elif vector.is_vertical:
                    steps += abs(point.y - vector.point_from.y)
                else:
                    # will not happen
                    pass
                return steps
            else:
                steps += vector.length
        return None

################################################################################

    def _intersections(self, other: Self) -> Tuple[Any, ...]:
        """
        :param other: other wire
        :return: all points of intersection with the other wire
        """

        return tuple(filter(
            lambda intersection:
            intersection is not None
            and (intersection.x != 0 or intersection.y != 0),
            tuple(vector1.get_intersection(vector2)
                  for vector1 in self._vectors
                  for vector2 in other.vectors)))

################################################################################
