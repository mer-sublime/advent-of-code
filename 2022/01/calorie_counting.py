"""https://adventofcode.com/2022/day/1"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class CalorieCounter:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        elves = []
        elve = []
        with open(self.input, 'r') as f:
            for line in f:
                if line == '\n':
                    elves.append(elve)
                    elve = []
                    continue
                elve.append(int(line))
            # Add last elve
            elves.append(elve)
        self.elves = elves

    def part_one(self):
        return max([sum(elve) for elve in self.elves])

    def part_two(self):
        elves_totals = [sum(elve) for elve in self.elves]
        elves_totals.sort(reverse=True)
        return sum(elves_totals[:3])


class TestCalorieCounter(TestCase):
    def test_part_one(self):
        self.assertEqual(24000, CalorieCounter(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(45000, CalorieCounter(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', CalorieCounter().part_one())
    print('Part Two:', CalorieCounter().part_two())
