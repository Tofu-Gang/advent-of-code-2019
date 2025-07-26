__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
An Intcode computer program consists of an instruction followed by zero or more
params. In the instruction, opcode is preceded by parameter modes: 0 for 
position mode, 1 for immediate mode. A param in position mode is treated as an 
address; in immediate mode it is just a value.

This helper class creates a simple object where both address and value is filled
in for position mode params and just a value is filled in for immediate mode 
params. 
"""


################################################################################

class Param:

    def __init__(self, value: int, address: int | None=None):
        """
        Create a param with both address and value (position mode) or just a
        value (immediate mode).

        :param value: param value
        :param address: address for position mode params or None for immediate
        mode params
        """

        self._address = address
        self._value = value

################################################################################

    @property
    def address(self) -> int | None:
        """
        :return: address for position mode params
        """

        return self._address

################################################################################

    @property
    def value(self) -> int | None:
        """
        :return: param value
        """

        return self._value

################################################################################
