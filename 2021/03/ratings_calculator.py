"""https://adventofcode.com/2021/day/3"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'
OXYGEN = 'OXYGEN'
CO2 = 'CO2'


class RatingsCalculator:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def part_one(self):
        sums = []
        size = 0
        with open(self.input, 'r') as f:
            for line in f:
                size += 1
                # sums = first line
                if not sums:
                    sums = [int(c) for c in line[:-1]]
                    continue
                # Increment each bit in sums
                for index, char in enumerate(line[:-1]):
                    sums[index] = sums[index] + int(char)

        # Determine half size
        half_size = int(size / 2)

        # Find gamma & epsilon rates

        gamma_rate = ''.join(['1' if bit > half_size else '0' for bit in sums])
        epsilon_rate = ''.join(['1' if bit < half_size else '0' for bit in sums])

        # Convert to base10 and return the product
        return int(gamma_rate, 2) * int(epsilon_rate, 2)

    def part_one_bis(self):
        sums = []
        size = 0
        with open(self.input, 'r') as f:
            for line in f:
                size += 1
                # sums = first line
                if not sums:
                    sums = [int(c) for c in line[:-1]]
                    continue
                # Increment each bit in sums
                for index, char in enumerate(line[:-1]):
                    sums[index] = sums[index] + int(char)

        # Determine half size
        half_size = int(size / 2)

        # Find gamma & epsilon rates
        gamma_rate = ''
        epsilon_rate = ''
        for bit in sums:
            if bit > half_size:
                gamma_rate += '1'
                epsilon_rate += '0'
            else:
                epsilon_rate += '1'
                gamma_rate += '0'

        # Convert to base10 and return the product
        return int(gamma_rate, 2) * int(epsilon_rate, 2)

    def part_two(self):
        with open(self.input, 'r') as f:
            lines = f.readlines()

        oxygen_generator_rating = part_two_compute_rating(lines=lines.copy(), gas=OXYGEN)
        co2_scrubber_rating = part_two_compute_rating(lines=lines.copy(), gas=CO2)

        # Convert to base10 and return the product
        return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


def part_two_compute_rating(lines, gas):
    line_length = len(lines[0])
    bit_criteria = ''
    for index in range(line_length):
        if 1 == (size := len(lines)):
            return lines[0]
        nb_1_bits = sum([int(line[index]) for line in lines])
        if nb_1_bits >= size / 2:
            bit_criteria += '1' if gas == OXYGEN else '0'
        else:
            bit_criteria += '0' if gas == OXYGEN else '1'
        lines = list(filter(lambda line: line.startswith(bit_criteria), lines))


class TestPowerConsumption(TestCase):
    def test_part_one(self):
        self.assertEqual(RatingsCalculator(test=True).part_one(), 198)

    def test_part_two(self):
        self.assertEqual(RatingsCalculator(test=True).part_two(), 230)


if __name__ == "__main__":
    print('Part One:', RatingsCalculator().part_one())
    print('Part Two:', RatingsCalculator().part_two())
