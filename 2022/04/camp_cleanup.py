"""https://adventofcode.com/2022/day/4"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class CampCleaner:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        with open(self.input, 'r') as f:
            sections_to_clean = [[range(int(sections.split('-')[0]), int(sections.split('-')[1]) + 1) for sections in line.split(',')]
                                 for line in f]

        self.groups = sections_to_clean

    def part_one(self):
        """Count pairs of assignments where one range fully contains the other."""
        return sum(set(range_1).issubset(range_2) or set(range_2).issubset(range_1) for range_1, range_2 in self.groups)

    def part_two(self):
        """Count pairs of assignments where both range overlap."""
        return sum(len(set(range_1).intersection(range_2)) > 0 for range_1, range_2 in self.groups)


class TestCanCleaner(TestCase):
    def test_part_one(self):
        self.assertEqual(2, CampCleaner(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(4, CampCleaner(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', CampCleaner().part_one())
    print('Part Two:', CampCleaner().part_two())
