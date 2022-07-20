"""https://adventofcode.com/2021/day/7"""
import math
import statistics
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


def sum_triangular(n):
    return n * (n + 1) // 2


class CrabSorting:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        with open(self.input, 'r') as f:
            self.crabs = list(map(int, f.readline().split(',')))

    def find_fuel_cost(self, pos):
        """n steps require n fuel units."""
        return sum([abs(crab - pos) for crab in self.crabs])

    def find_fuel_cost_triangular(self, pos):
        """n steps require n(n + 1) / 2 fuel units."""
        # return sum([sum(range(abs(crab - pos) + 1)) for crab in self.crabs])
        return sum([sum_triangular(abs(crab - pos)) for crab in self.crabs])

    def part_one(self):
        """Find how much fuel is needed by each crab to reach target position."""
        return self.find_fuel_cost(pos=int(statistics.median(self.crabs)))

    def part_two(self):
        """Find how much fuel is needed by each crab to reach target position."""
        mean = statistics.mean(self.crabs)
        floor_mean, ceil_mean = math.floor(mean), math.ceil(mean)

        # print(f'{mean = }')
        # print(f'Floor: {floor_mean} -> {self.find_fuel_cost_triangular(pos=floor_mean)}')
        # print(f'Ceil: {ceil_mean} -> {self.find_fuel_cost_triangular(pos=ceil_mean)}')

        return min(
            self.find_fuel_cost_triangular(pos=floor_mean),
            self.find_fuel_cost_triangular(pos=ceil_mean)
        )

    def part_two_brute_force_for(self):
        # Find all potential target positions.
        positions = range(min(self.crabs), max(self.crabs) + 1)

        # Try them all. Brute force rocks.
        best_result = max(self.crabs) ** 3
        for pos in positions:
            # Find the amount of fuel needed for all crabs to reach target position.
            fuel = self.find_fuel_cost_triangular(pos=pos)

            # Keep the lowest value.
            best_result = min(fuel, best_result)

            if fuel > best_result:    # When the result gets worse, return the previous value.
                return best_result

    def part_two_brute_force_while(self):
        pos = min(self.crabs)
        fuel = self.find_fuel_cost_triangular(pos)
        # Try all possible positions until the fuel value stops decreasing.
        while fuel >= (next_fuel := self.find_fuel_cost_triangular(pos + 1)):
            pos += 1
            fuel = next_fuel    # Save next result for the next iteration.

        return fuel


class TestCrabSorting(TestCase):
    def test_part_one(self):
        self.assertEqual(37, CrabSorting(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(168, CrabSorting(test=True).part_two())

    def test_part_two_brute_force(self):
        self.assertEqual(168, CrabSorting(test=True).part_two_brute_force_for())
        self.assertEqual(168, CrabSorting(test=True).part_two_brute_force_while())


if __name__ == "__main__":
    print('Part One:', CrabSorting().part_one())
    print('Part Two:', CrabSorting().part_two())
    print('Part Two (BF for):', CrabSorting().part_two_brute_force_for())
    print('Part Two (BF while):', CrabSorting().part_two_brute_force_while())
