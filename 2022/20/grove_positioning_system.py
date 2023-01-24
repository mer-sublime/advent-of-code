"""https://adventofcode.com/2022/day/20"""
import itertools
from dataclasses import dataclass
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


@dataclass
class Number:
    value: int

    def __add__(self, other):
        """Can be added like regular int instances."""
        return self.value + other

    def __eq__(self, other):
        """Differentiate instances based on memory address, not on value."""
        return id(self) == id(other)


class FileDecryptor:
    def __init__(self, test=False):
        self.encrypted_values = []
        self.parse_input(input_file=TEST_INPUT_FILE if test else INPUT_FILE)

    def parse_input(self, input_file):
        with open(input_file, 'r') as f:
            self.encrypted_values = [Number(int(line)) for line in f]

    def decrypt_values(self):
        values = self.encrypted_values.copy()
        size_after_pop = len(values) - 1
        for number in self.encrypted_values:
            index = values.index(number)
            new_index = number + index
            values.pop(index)

            if abs(new_index) > size_after_pop:
                new_index = new_index % size_after_pop
            if new_index == 0:  # Position 0 = at the end in the given example.
                values.append(number.value)
            else:
                values.insert(new_index, number.value)
        return values

    @staticmethod
    def get_coordinates(values):
        if not values:
            return

        c = itertools.cycle(values)
        while next(c) != 0:  # Start at the first 0 encountered
            continue
        print(values)
        print(list(itertools.islice(c, 999, 3001, 1000)))
        return sum(itertools.islice(c, 999, 3001, 1000))  # 1000th, 2000th and 3000th values after 0

    def part_one(self):
        return self.get_coordinates(values=self.decrypt_values())


class TestFileDecryptor(TestCase):
    def test_get_coordinates(self):
        values = [1, 2, -3, 4, 0, 3, -2]
        self.assertEqual(3, FileDecryptor.get_coordinates(values))

    def test_decrypt_values(self):
        self.assertEqual([1, 2, -3, 4, 0, 3, -2], FileDecryptor(test=True).decrypt_values())

    def test_part_one(self):
        self.assertEqual(3, FileDecryptor(test=True).part_one())


if __name__ == '__main__':
    print('Part One:', FileDecryptor().part_one())
    # print('Part Two:', FileDecryptor().part_two())
