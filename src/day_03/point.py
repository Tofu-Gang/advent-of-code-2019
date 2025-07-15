__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"


################################################################################

class Point:

    def __init__(self, x: int, y: int):
        """
        A point is defined by horizontal (x) and vertical (y) axis positions.

        :param x: horizontal axis position
        :param y: vertical axis position
        """

        self._x = x
        self._y = y

################################################################################

    @property
    def x(self) -> int:
        """
        :return: horizontal axis position
        """

        return self._x

################################################################################

    @property
    def y(self) -> int:
        """
        :return: vertical axis position
        """

        return self._y

################################################################################
