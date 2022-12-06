"""https://adventofcode.com/2022/day/"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class PuzzleSolver:
    def __init__(self, test=False):
        self.parse_input(TEST_INPUT_FILE if test else INPUT_FILE)

    def parse_input(self):
        with open(self.input, 'r') as f:
            for line in f:
                pass

    def part_one(self):
        pass

    def part_two(self):
        pass


class TestPuzzleSolver(TestCase):
    def test_part_one(self):
        self.assertEqual(True, PuzzleSolver(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(True, PuzzleSolver(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', PuzzleSolver().part_one())
    print('Part Two:', PuzzleSolver().part_two())
