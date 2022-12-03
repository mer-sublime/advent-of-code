"""https://adventofcode.com/2022/day/3"""
import string
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class RucksackReorganizer:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    letter_scores = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

    def part_one(self):
        with open(self.input, 'r') as f:
            misplaced_letters = [next(iter(set(line[len(line) // 2:]).intersection(line[:len(line) // 2])))
                                 for line in f]
        return sum(self.letter_scores[letter] for letter in misplaced_letters)

    def part_two(self):
        with open(self.input, 'r') as f:
            elves_groups = list(zip(*[f]*3))
        badges = [next(iter(set(group[0].rstrip()).intersection(group[1].rstrip()).intersection(group[2].rstrip())))
                  for group in elves_groups]
        return sum(self.letter_scores[letter] for letter in badges)


class TestRucksackReorganizer(TestCase):
    def test_part_one(self):
        self.assertEqual(157, RucksackReorganizer(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(70, RucksackReorganizer(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', RucksackReorganizer().part_one())
    print('Part Two:', RucksackReorganizer().part_two())
