"""https://adventofcode.com/2021/day/"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class Puzzle:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        with open(self.input, 'r') as f:
            for line in f:
                pass

    def part_one(self):
        pass

    def part_two(self):
        pass


class TestPuzzle(TestCase):
    def test_part_one(self):
        self.assertEqual(True, Puzzle(test=True).part_one())

    # def test_part_two(self):
    #     self.assertEqual(True, Puzzle(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', Puzzle().part_one())
    # print('Part Two:', Puzzle().part_two())
