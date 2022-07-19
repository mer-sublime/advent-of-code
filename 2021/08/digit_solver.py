"""https://adventofcode.com/2021/day/8"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class DigitSolver:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def part_one(self):
        count_1_4_7_8 = 0
        with open(self.input, 'r') as f:
            for line in f:
                output = line.split('|')[1].split()
                count_1_4_7_8 += sum(1 for digit in output if len(digit) in (2, 3, 4, 7))
        return count_1_4_7_8

    def part_two(self):
        total = 0
        with open(self.input, 'r') as f:
            for line in f:
                digits, output = line.split('|')
                digits = digits.split()
                output = output.split()
                key = self.find_key(digits=digits)
                total += self.resolve(output=output, key=key)
        return total

    @staticmethod
    def find_key(digits):
        key = [''] * 10

        # Sort input by length.
        input_lengths = {k: [] for k in range(2, 8)}
        for digit in digits:
            input_lengths[len(digit)].append(set(digit))

        # Find 1, 4, 7 and 8.
        key[1] = input_lengths[2].pop()
        key[4] = input_lengths[4].pop()
        key[7] = input_lengths[3].pop()
        key[8] = input_lengths[7].pop()

        # 6 is the only 6-sized digit that does not contain 1.
        key[6] = next(digit for digit in input_lengths[6] if not key[1] < digit)
        # 9 is the only 6-sized digit that contains 4.
        key[9] = next(digit for digit in input_lengths[6] if key[4] < digit)
        # 0 is the remaining 6-sized digit.
        key[0] = next(digit for digit in input_lengths[6] if digit != key[6] and digit != key[9])

        # 3 is the only 5-sized digit that contains 1.
        key[3] = next(digit for digit in input_lengths[5] if key[1] < digit)
        # 5 is the only 5-sized digit contained by 6.
        key[5] = next(digit for digit in input_lengths[5] if digit < key[6])
        # 2 is the remaining 5-sized digit.
        key[2] = next(digit for digit in input_lengths[5] if digit != key[3] and digit != key[5])

        return key


    @staticmethod
    def resolve(output, key):
        output = [str(key.index(set(digit))) for digit in output]
        return int(''.join(output))


class TestDigitSolver(TestCase):
    def test_part_one(self):
        self.assertEqual(DigitSolver(test=True).part_one(), 26)

    def test_part_two(self):
        self.assertEqual(DigitSolver(test=True).part_two(), 61229)


if __name__ == "__main__":
    print('Part One:', DigitSolver().part_one())
    print('Part Two:', DigitSolver().part_two())
