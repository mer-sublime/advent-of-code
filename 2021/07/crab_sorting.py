"""https://adventofcode.com/2021/day/7"""
from unittest import TestCase
import statistics, math

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class CrabSorting:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def part_one(self):
        with open(self.input, 'r') as f:
            crabs = list(map(int, f.readline().split(',')))

            # Find median position
            target_position = statistics.median(crabs)
            #
            # crabs.sort()
            # n_crabs = len(crabs)
            # if n_crabs % 2:
            #     median_position = crabs[int((n_crabs + 1) / 2)]
            # else:
            #     median_position = crabs[int(n_crabs / 2)]

            # Return the sum of steps needed by each crab to reach target position
            return sum([abs(crab - target_position) for crab in crabs])

    def part_two(self):
        with open(self.input, 'r') as f:
            crabs = list(map(int, f.readline().split(',')))

            # Find all possible values for target position.
            possible_crab_positions = range(min(crabs), max(crabs) + 1)

            # Try them all. Brute force rocks.
            for target_position in possible_crab_positions:
                # Return the amount of fuel needed by each crab to reach target position
                fuel = sum([sum(range(abs(crab - target_position) + 1)) for crab in crabs])
                # Is it our best result yet?
                if 'best_result' not in locals() or fuel < best_result:
                    best_result = fuel
            return best_result

    # def part_two(self):
    #     with open(self.input, 'r') as f:
    #         crabs = list(map(int, f.readline().split(',')))
    #
    #         square_crabs = None
    #         avg_crab = round(math.sqrt(round(sum(square_crabs) / len(crabs))))
    #
    #         return sum([sum(range(abs(crab - avg_crab) + 1)) for crab in crabs])


class TestCrabSorting(TestCase):
    def test_part_one(self):
        self.assertEqual(CrabSorting(test=True).part_one(), 37)

    def test_part_two(self):
        self.assertEqual(CrabSorting(test=True).part_two(), 168)


if __name__ == "__main__":
    print('Part One:', CrabSorting().part_one())
    print('Part Two:', CrabSorting().part_two())
