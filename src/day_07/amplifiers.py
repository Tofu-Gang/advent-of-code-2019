__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple
from threading import Condition
from src.intcode_computer.intcode_computer import IntcodeComputer


class Amplifiers:

################################################################################

    def __init__(self, program: str, phase_settings: Tuple[int]):
        """
        Create the same number of amplifiers (intcode computer instances) as is
        the number of phase settings. Load the Amplifier Controller Software and
        set phase settings as corresponding amplifier input values.

        :param program: Amplifier Controller Software
        :param phase_settings: phase settings for each amplifier
        """

        self._output_condition = Condition()
        self._amplifiers = tuple(IntcodeComputer(self._output_condition)
                                 for _ in range(len(phase_settings)))
        [amplifier.load_program(program) for amplifier in self._amplifiers]
        [self._amplifiers[i].set_input(phase_settings[i])
         for i in range(len(self._amplifiers))]

################################################################################

    def configure(self) -> None:
        """
        Run the Amplifier Controller Software on each amplifier, using each
        amplifier output value as an input value for the next one. The first
        amplifier input value is zero; depending on phase settings, output value
        from the last amplifier can be also fed as an input of the first one.
        """

        input_signal = 0
        [amplifier.start() for amplifier in self._amplifiers]

        while any(amplifier.is_alive() for amplifier in self._amplifiers):
            for i in range(len(self._amplifiers)):
                amplifier = self._amplifiers[i]

                with self._output_condition:
                    amplifier.set_input(input_signal)
                    self._output_condition.wait()
                input_signal = amplifier.output[-1]

################################################################################

    @property
    def thrusters_signal(self) -> int:
        """
        :return: the last amplifier output signal that is connected to the
        thrusters
        """

        return self._amplifiers[-1].output[-1]

################################################################################
