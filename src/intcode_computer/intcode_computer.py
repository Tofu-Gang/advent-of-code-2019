__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
Intcode computer is a computer which processes Intcode programs. An Intcode 
program is a list of integers separated by commas.
"""


################################################################################

class IntcodeComputer:
    SEPARATOR = ","

################################################################################

    def __init__(self):
        """
        Initialize an empty memory. The address of the current instruction is
        called the instruction pointer; it starts at 0. Associate opcodes with
        their instructions.
        """

        self._memory = []
        self._instruction_pointer = 0
        self._running = False

        self.OPCODES = {
            1: self._addition,
            2: self._multiplication,
            99: self._terminate
        }

################################################################################

    def get_value(self, address: int) -> int:
        """
        :param address: a memory address
        :return: a value in the specified address
        """

        return self._memory[address]

################################################################################

    def load_program(self, program: str) -> None:
        """
        Initialize memory to the program's values.

        :param program: an Intcode program
        """

        self._memory = list(map(int, program.split(self.SEPARATOR)))

################################################################################

    def run_program(self) -> None:
        """
        To run an Intcode program, start by looking at the first integer (called
        position 0). Here, you will find an opcode. Opcodes mark the beginning
        of an instruction. The values used immediately after an opcode, if any,
        are called the instruction's parameters.

        Encountering an unknown opcode means something went wrong. Once you're
        done processing an instruction, move to the next one by stepping forward
        to the address right after the instruction parameters.
        """

        self._running = True

        while self._running:
            opcode = self._memory[self._instruction_pointer]
            instruction = self.OPCODES[opcode]
            instruction()

################################################################################

    def reset(self) -> None:
        """
        Wipe the memory clean and set the instruction pointer back to zero.
        """

        self._memory = []
        self._instruction_pointer = 0
        self._running = False

################################################################################

    def set_input(self, address: int, value: int) -> None:
        """
        Set a value in the specified address.

        :param address: an address
        :param value: a value
        """

        self._memory[address] = value

################################################################################

    def _addition(self) -> None:
        """
        Opcode 1 adds together numbers read from two addresses and stores the
        result in a third address. The three integers immediately after the
        opcode tell you these three addresses - the first two indicate the
        addresses from which you should read the input values, and the third
        indicates the position at which the output should be stored.
        """

        address_1 = self._memory[self._instruction_pointer + 1]
        address_2 = self._memory[self._instruction_pointer + 2]
        param_1 = self._memory[address_1]
        param_2 = self._memory[address_2]
        result_address = self._memory[self._instruction_pointer + 3]
        self._memory[result_address] = param_1 + param_2
        self._instruction_pointer += 4

################################################################################

    def _multiplication(self) -> None:
        """
        Opcode 2 works exactly like opcode 1, except it multiplies the two
        inputs instead of adding them. Again, the three integers after the
        opcode indicate where the inputs and outputs are, not their values.
        """

        address_1 = self._memory[self._instruction_pointer + 1]
        address_2 = self._memory[self._instruction_pointer + 2]
        param_1 = self._memory[address_1]
        param_2 = self._memory[address_2]
        result_address = self._memory[self._instruction_pointer + 3]
        self._memory[result_address] = param_1 * param_2
        self._instruction_pointer += 4

################################################################################

    def _terminate(self) -> None:
        """
        Opcode 99 means that the program is finished and should immediately
        halt.
        """

        self._running = False

################################################################################
