"""https://adventofcode.com/2022/day/5"""
import re
from abc import ABC, abstractmethod
from collections import deque
from itertools import zip_longest
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class CargoCrane(ABC):
    INSTRUCTION_PATTERN = r'move (\d+) from (\d) to (\d)'

    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.stacks = []
        self.instructions = []
        with open(self.input, 'r') as f:
            self.parse_stacks(f)
            next(f)  # Skip empty line
            self.parse_instructions(f)

    def parse_stacks(self, file):
        stacks = []
        # Parse until the line with the stacks number
        while (line := next(file).rstrip())[1] != '1':
            stacks.insert(0, [line[i] for i in range(1, len(line), 4)])
        stacks = list(zip_longest(*stacks, fillvalue=' '))
        self.stacks = [deque(crate for crate in stack if crate != ' ') for stack in stacks]

    def parse_instructions(self, file):
        instructions = []
        for line in file:
            instruction = re.match(pattern=self.INSTRUCTION_PATTERN, string=line.rstrip())
            instructions.append({
                'quantity': int(instruction[1]),
                'from_stack': int(instruction[2]),
                'to_stack': int(instruction[3])})
        self.instructions = instructions

    def rearrange_stacks(self):
        for instruction in self.instructions:
            self.move_crates(**instruction)
        return ''.join(stack[-1] for stack in self.stacks)

    @abstractmethod
    def move_crates(self, quantity: int, from_stack: int, to_stack: int):
        pass


class CrateMover9000(CargoCrane):
    """A cargo crate that can move crates one at a time."""

    def move_crates(self, quantity: int, from_stack: int, to_stack: int):
        """Move crates, but one at a time, from a stack to another."""
        source = self.stacks[from_stack - 1]
        destination = self.stacks[to_stack - 1]
        for _ in range(quantity):
            destination.append(source.pop())


class CrateMover9001(CargoCrane):
    """A cargo crate that can move multiple crates at once."""

    def move_crates(self, quantity: int, from_stack: int, to_stack: int):
        """Move multiple crates at once from a stack to another."""
        source = self.stacks[from_stack - 1]
        destination = self.stacks[to_stack - 1]
        crates_to_move = reversed([source.pop() for _ in range(quantity)])
        destination.extend(crates_to_move)


class TestCargoCrane(TestCase):
    def test_part_one(self):
        self.assertEqual('CMZ', CrateMover9000(test=True).rearrange_stacks())

    def test_part_two(self):
        self.assertEqual('MCD', CrateMover9001(test=True).rearrange_stacks())


if __name__ == '__main__':
    print('Part One:', CrateMover9000().rearrange_stacks())
    print('Part Two:', CrateMover9001().rearrange_stacks())
