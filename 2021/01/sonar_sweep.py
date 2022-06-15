"""https://adventofcode.com/2021/day/1"""
from unittest import TestCase
from unittest.mock import patch


class SolarSweep:
    def __init__(self):
        self.input = self.get_input()

    @staticmethod
    def get_input():
        with open('input.txt', 'r') as file:
            return [int(line) for line in file]

    def part_one(self):
        has_increased_list = [value > self.input[index - 1] for index, value in enumerate(self.input) if index > 0]
        return sum(has_increased_list)

    def part_two(self):
        measurements = [sum(self.input[i:i+2]) for i in range(len(self.input[:-2]))]
        has_increased_list = [value > measurements[i-1] for i, value in enumerate(measurements) if i > 0]
        return sum(has_increased_list)


class TestSolarSweep(TestCase):
    input = (199, 200, 208, 210, 200, 207, 240, 269, 260, 263)

    @patch.object(SolarSweep, 'get_input', return_value=input)
    def test_part_one(self, _):
        self.assertEqual(SolarSweep().part_one(), 7)

    @patch.object(SolarSweep, 'get_input', return_value=input)
    def test_part_two(self, _):
        self.assertEqual(SolarSweep().part_two(), 5)


if __name__ == "__main__":
    print('Part One:', SolarSweep().part_one())
    print('Part Two:', SolarSweep().part_two())
