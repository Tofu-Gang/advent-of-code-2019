__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Self
from src.day_03.point import Point


################################################################################

class Vector:
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'
    KEY_POINT_TO = "POINT_TO"
    KEY_ORIENTATION = "ORIENTATION"
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    DIRECTIONS = {
        UP: {
            KEY_POINT_TO: lambda point_from, distance:
            Point(point_from.x, point_from.y + distance),
            KEY_ORIENTATION: VERTICAL
        },
        DOWN: {
            KEY_POINT_TO: lambda point_from, distance:
            Point(point_from.x, point_from.y - distance),
            KEY_ORIENTATION: VERTICAL
        },
        LEFT: {
            KEY_POINT_TO: lambda point_from, distance:
            Point(point_from.x - distance, point_from.y),
            KEY_ORIENTATION: HORIZONTAL
        },
        RIGHT: {
            KEY_POINT_TO: lambda point_from, distance:
            Point(point_from.x + distance, point_from.y),
            KEY_ORIENTATION: HORIZONTAL
        }
    }

################################################################################

    def __init__(self, direction: str, distance: int, point_from: Point):
        """
        A vector is defined by two points, has a direction (one of four main
        directions up, down, left, right), length and is either horizontal or
        vertical.
        """

        self._direction = direction
        self._length = distance
        self._point_from = point_from

################################################################################

    @property
    def length(self) -> int:
        """
        :return: vector length
        """

        return self._length

################################################################################

    @property
    def point_from(self) -> Point:
        """
        :return: vector start point
        """

        return self._point_from

################################################################################

    @property
    def point_to(self) -> Point:
        """
        :return: vector end point
        """

        get_point_to = self.DIRECTIONS[self._direction][self.KEY_POINT_TO]
        return get_point_to(self._point_from, self._length)

################################################################################

    @property
    def orientation(self) -> str:
        """
        :return: horizontal or vertical string constant
        """

        return self.DIRECTIONS[self._direction][self.KEY_ORIENTATION]

################################################################################

    @property
    def is_horizontal(self) -> bool:
        """
        :return: True if the vector is horizontal, False otherwise
        """

        return self.orientation == self.HORIZONTAL

################################################################################

    @property
    def is_vertical(self) -> bool:
        """
        :return: True if the vector is vertical, False otherwise
        """

        return self.orientation == self.VERTICAL

################################################################################

    @property
    def fixed(self) -> int:
        """
        :return: x or y value that is the same for both vector points (x value
        for vertical vectors, y value for horizontal vectors)
        """

        if self.is_horizontal:
            return self.point_from.y
        elif self.is_vertical:
            return self.point_from.x
        else:
            # will not happen
            return -1

################################################################################

    def get_intersection(self, other: Self) -> Point | None:
        """
        :param other: the other vector
        :return: intersection point of this and other vector or None if there is
        no intersection point
        """

        if self.orientation != other.orientation:
            if self.is_horizontal:
                from_x = min(self.point_from.x, self.point_to.x)
                to_x = max(self.point_from.x, self.point_to.x)
                from_y = min(other.point_from.y, other.point_to.y)
                to_y = max(other.point_from.y, other.point_to.y)

                if from_x <= other.fixed <= to_x and from_y <= self.fixed < to_y:
                    return Point(other.fixed, self.fixed)
                else:
                    return None
            elif self.is_vertical:
                from_x = min(other.point_from.x, other.point_to.x)
                to_x = max(other.point_from.x, other.point_to.x)
                from_y = min(self.point_from.y, self.point_to.y)
                to_y = max(self.point_from.y, self.point_to.y)

                if from_x <= self.fixed < to_x and from_y <= other.fixed < to_y:
                    return Point(self.fixed, other.fixed)
                else:
                    return None
            else:
                return None
        else:
            return None

################################################################################

    def contains_point(self, point: Point) -> bool:
        """
        :param point: a point
        :return: True if this vector contains the point, False otherwise
        """
        from_x = min(self._point_from.x, self.point_to.x)
        to_x = max(self._point_from.x, self.point_to.x)
        from_y = min(self._point_from.y, self.point_to.y)
        to_y = max(self._point_from.y, self.point_to.y)
        return from_x <= point.x <= to_x and from_y <= point.y <= to_y

################################################################################
