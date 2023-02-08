"""https://adventofcode.com/2022/day/20"""
import itertools
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class FileDecryptor:
    def __init__(self, test=False):
        self.instructions = []
        self.parse_input(input_file=TEST_INPUT_FILE if test else INPUT_FILE)

    def parse_input(self, input_file):
        with open(input_file, 'r') as f:
            values = [int(line) for line in f]
        self.instructions = [t for t in enumerate(values)]

    def mix(self, rounds=1):
        values = self.instructions.copy()
        size_after_pop = len(values) - 1
        for num_tuple in self.instructions * rounds:
            index = values.index(num_tuple)
            new_index = (num_tuple[1] + index) % size_after_pop
            values.pop(index)
            # If new index = 0 -> move at the end of the list.
            if new_index == 0:
                values.append(num_tuple)
            else:
                values.insert(new_index, num_tuple)
        return values

    @staticmethod
    def get_coordinates(values):
        """Return the sum of the 1000th, 2000th and 3000th values after the first 0."""
        if not values:
            return

        c = itertools.cycle(values)
        while next(c)[1] != 0:  # Start at the first 0 encountered
            continue
        return sum(num_tuple[1] for num_tuple in itertools.islice(c, 999, 3000, 1000))

    def part_one(self):
        return self.get_coordinates(values=self.mix())

    def part_two(self):
        key = 811589153
        self.instructions = [(index, value * key) for index, value in self.instructions]
        return self.get_coordinates(values=self.mix(rounds=10))


class TestFileDecryptor(TestCase):
    def test_get_coordinates(self):
        values = enumerate([1, 2, -3, 4, 0, 3, -2])
        self.assertEqual(3, FileDecryptor.get_coordinates(values))

    def test_mix(self):
        self.assertEqual([1, 2, -3, 4, 0, 3, -2], [num_tuple[1] for num_tuple in FileDecryptor(test=True).mix()])

    def test_part_one(self):
        self.assertEqual(3, FileDecryptor(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(1623178306, FileDecryptor(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', FileDecryptor().part_one())
    print('Part Two:', FileDecryptor().part_two())
