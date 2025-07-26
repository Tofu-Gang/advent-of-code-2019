__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
Intcode computer is a computer which processes Intcode programs. An Intcode 
program is a list of integers separated by commas.
"""

from typing import Tuple
from src.intcode_computer.param import Param


################################################################################

class IntcodeComputer:
    SEPARATOR = ","
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1
    KEY_METHOD = "METHOD"
    KEY_PARAMS_COUNT = "PARAMS_COUNT"

    # OPCODES
    ADDITION = 1
    MULTIPLICATION = 2
    STORE_INPUT = 3
    STORE_OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    TERMINATE = 99

################################################################################

    def __init__(self):
        """
        Initialize an empty memory, input and output. The address of the current
        instruction is called the instruction pointer; it starts at 0. Associate
        opcodes with their instructions.
        """

        self._memory = []
        self._input = None
        self._output = []
        self._instruction_pointer = 0
        self._running = False

        self.OPCODES = {
            self.ADDITION: {
                self.KEY_METHOD: self._addition,
                self.KEY_PARAMS_COUNT: 3
            },
            self.MULTIPLICATION: {
                self.KEY_METHOD: self._multiplication,
                self.KEY_PARAMS_COUNT: 3
            },
            self.STORE_INPUT: {
                self.KEY_METHOD: self._store_input,
                self.KEY_PARAMS_COUNT: 1
            },
            self.STORE_OUTPUT: {
                self.KEY_METHOD: self._store_output,
                self.KEY_PARAMS_COUNT: 1
            },
            self.JUMP_IF_TRUE: {
                self.KEY_METHOD: self._jump_if_true,
                self.KEY_PARAMS_COUNT: 2
            },
            self.JUMP_IF_FALSE: {
                self.KEY_METHOD: self._jump_if_false,
                self.KEY_PARAMS_COUNT: 2
            },
            self.LESS_THAN: {
                self.KEY_METHOD: self._less_than,
                self.KEY_PARAMS_COUNT: 3
            },
            self.EQUALS: {
                self.KEY_METHOD: self._equals,
                self.KEY_PARAMS_COUNT: 3
            },
            self.TERMINATE: {
                self.KEY_METHOD: self._terminate,
                self.KEY_PARAMS_COUNT: 0
            }
        }

################################################################################

    @property
    def output(self) -> Tuple[int]:
        """
        :return: output values
        """

        return tuple(self._output)

################################################################################

    def get_value(self, address: int) -> int:
        """
        :param address: a memory address
        :return: a value in the specified address
        """

        return self._memory[address]

################################################################################

    def set_value(self, address: int, value: int) -> None:
        """
        Set a value in the specified address.

        :param address: an address
        :param value: a value
        """

        self._memory[address] = value

################################################################################

    def set_input(self, value: int) -> None:
        """
        Set an input value.

        :param value: an input value
        """

        self._input = value

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
            opcode = self._get_opcode()
            method = self.OPCODES[opcode][self.KEY_METHOD]
            method()

################################################################################

    def reset(self) -> None:
        """
        Wipe the memory, input and output clean and set the instruction pointer
        back to zero.
        """

        self._memory = []
        self._input = None
        self._output = []
        self._instruction_pointer = 0
        self._running = False

################################################################################

    def _get_opcode(self) -> int:
        """
        :return: current instruction opcode
        """

        return int(str(self._memory[self._instruction_pointer])[-2:])

################################################################################

    def _get_instruction(self) -> str:
        """
        :return: current instruction with all param modes
        """

        opcode = self._get_opcode()
        params_count = self.OPCODES[opcode][self.KEY_PARAMS_COUNT]
        return f"{self._memory[self._instruction_pointer]:0{params_count + 2}d}"

################################################################################

    def _get_params(self) -> Tuple[Param]:
        """
        :return: current instruction params
        """

        opcode = self._get_opcode()
        params_count = self.OPCODES[opcode][self.KEY_PARAMS_COUNT]
        instruction = self._get_instruction()
        params = []

        for i in range(1, params_count + 1):
            param_mode = int(instruction[-2 - i])

            if param_mode == self.POSITION_MODE:
                address = self._memory[self._instruction_pointer + i]
                value = self._memory[address]
                params.append(Param(value, address=address))
            elif param_mode == self.IMMEDIATE_MODE:
                value = self._memory[self._instruction_pointer + i]
                params.append(Param(value))

        return tuple(params)

################################################################################

    def _jump_to_next_instruction(self, opcode: int) -> None:
        """
        Move instruction pointer to the beginning of the next instruction.

        :param opcode: current instruction opcode; is needed to get number of
        params of the current instruction; must be stated explicitly because it
        can be overwritten while processing the current instruction
        """

        params_count = self.OPCODES[opcode][self.KEY_PARAMS_COUNT]
        self._instruction_pointer += (params_count + 1)

################################################################################

    def _addition(self) -> None:
        """
        Opcode 1 adds together numbers read from two addresses and stores the
        result in a third address. The three integers immediately after the
        opcode tell you these three addresses - the first two indicate the
        addresses from which you should read the input values, and the third
        indicates the position at which the output should be stored.
        """

        param1, param2, param3 = self._get_params()
        self._memory[param3.address] = param1.value + param2.value
        self._jump_to_next_instruction(self.ADDITION)

################################################################################

    def _multiplication(self) -> None:
        """
        Opcode 2 works exactly like opcode 1, except it multiplies the two
        inputs instead of adding them. Again, the three integers after the
        opcode indicate where the inputs and outputs are, not their values.
        """

        param1, param2, param3 = self._get_params()
        self._memory[param3.address] = param1.value * param2.value
        self._jump_to_next_instruction(self.MULTIPLICATION)

################################################################################

    def _store_input(self) -> None:
        """
        Opcode 3 takes a single integer as input and saves it to the position
        given by its only parameter.
        """

        param = self._get_params()[0]
        self._memory[param.address] = self._input
        self._jump_to_next_instruction(self.STORE_INPUT)

################################################################################

    def _store_output(self) -> None:
        """
        Opcode 4 outputs the value of its only parameter.
        """

        param = self._get_params()[0]
        self._output.append(param.value)
        self._jump_to_next_instruction(self.STORE_OUTPUT)

################################################################################

    def _jump_if_true(self) -> None:
        """
        Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets
        the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
        """

        param1, param2 = self._get_params()

        if param1.value != 0:
            self._instruction_pointer = param2.value
        else:
            self._jump_to_next_instruction(self.JUMP_IF_TRUE)

################################################################################

    def _jump_if_false(self) -> None:
        """
        Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
        instruction pointer to the value from the second parameter. Otherwise,
        it does nothing.
        """

        param1, param2 = self._get_params()

        if param1.value == 0:
            self._instruction_pointer = param2.value
        else:
            self._jump_to_next_instruction(self.JUMP_IF_FALSE)

################################################################################

    def _less_than(self) -> None:
        """
        Opcode 7 is less than: if the first parameter is less than the second
        parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0.
        """

        param1, param2, param3 = self._get_params()

        if param1.value < param2.value:
            self._memory[param3.address] = 1
        else:
            self._memory[param3.address] = 0

        self._jump_to_next_instruction(self.LESS_THAN)

################################################################################

    def _equals(self) -> None:
        """
        Opcode 8 is equals: if the first parameter is equal to the second
        parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0.
        """

        param1, param2, param3 = self._get_params()

        if param1.value == param2.value:
            self._memory[param3.address] = 1
        else:
            self._memory[param3.address] = 0

        self._jump_to_next_instruction(self.EQUALS)

################################################################################

    def _terminate(self) -> None:
        """
        Opcode 99 means that the program is finished and should immediately
        halt.
        """

        self._running = False

################################################################################
