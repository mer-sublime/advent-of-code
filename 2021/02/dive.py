"""https://adventofcode.com/2021/day/2"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class Dive:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def part_one(self):
        position, depth = 0, 0
        with open(self.input, 'r') as file:
            for instruction in file:
                move, value = instruction.split()
                value = int(value)
                if move == 'forward':
                    position += value
                elif move == 'up':
                    depth -= value
                elif move == 'down':
                    depth += value
        return position * depth

    def part_two(self):
        position, depth, aim = 0, 0, 0
        with open(self.input, 'r') as file:
            for instruction in file:
                move, value = instruction.split()
                value = int(value)
                if move == 'forward':
                    position += value
                    depth += aim * value
                elif move == 'up':
                    aim -= value
                elif move == 'down':
                    aim += value
        return position * depth


class Submarine:
    position = 0
    depth = 0
    aim = 0

    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def move(self):
        with open(self.input, 'r') as file:
            for instruction in file:
                command, value = instruction.split()
                getattr(self, command)(int(value))

        return self.position * self.depth

    def forward(self, value):
        self.position += value
        self.depth += self.aim * value

    def up(self, value):
        self.aim -= value

    def down(self, value):
        self.aim += value


class TestDive(TestCase):

    def test_part_one(self):
        self.assertEqual(150, Dive(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(900, Dive(test=True).part_two())
        self.assertEqual(900, Submarine(test=True).move())


if __name__ == "__main__":
    print('Part One:', Dive().part_one())
    print('Part Two:', Dive().part_two())
    print('Part Two:', Submarine().move())
