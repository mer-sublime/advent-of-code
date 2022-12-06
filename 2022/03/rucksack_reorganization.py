"""https://adventofcode.com/2022/day/3"""
import string
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class RucksackReorganizer:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    type_priorities = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

    def part_one(self) -> int:
        """Find the priority of every item types found in both compartments of a rucksack."""
        with open(self.input, 'r') as f:
            misplaced_types = [next(iter(set(line[len(line) // 2:]).intersection(line[:len(line) // 2])))
                               for line in f]
        return sum(self.type_priorities[item_type] for item_type in misplaced_types)

    def part_two(self) -> int:
        """Find the priority of every badge given to each group of 3 rucksacks."""
        with open(self.input, 'r') as f:
            rucksack_groups = list(zip(*[f]*3))
        badges = [next(iter(set(group[0].rstrip()).intersection(group[1].rstrip()).intersection(group[2].rstrip())))
                  for group in rucksack_groups]
        return sum(self.type_priorities[letter] for letter in badges)


class TestRucksackReorganizer(TestCase):
    def test_part_one(self):
        self.assertEqual(157, RucksackReorganizer(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(70, RucksackReorganizer(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', RucksackReorganizer().part_one())
    print('Part Two:', RucksackReorganizer().part_two())
