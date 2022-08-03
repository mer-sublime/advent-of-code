"""https://adventofcode.com/2021/day/9"""
from enum import Enum
from unittest import TestCase
import math

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


def get_low_points_in_line(line_number, line, prev_line=None, next_line=None):
    low_points = []
    for point in SmokeMapper.get_low_points_candidates(line_number=line_number, line=line):
        if (not prev_line or point.value < prev_line[point.y]) and (not next_line or point.value < next_line[point.y]):
            low_points.append(point)
    return low_points


def get_risk_level(low_points):
    return sum([point.risk_level for point in low_points])


class Point:
    def __init__(self, x, y, value):
        self.x, self.y, self.value = x, y, value
        self.risk_level = value + 1

    def __repr__(self):
        return f'({self.x}; {self.y}): {self.value}'


class Direction(Enum):
    UP = '↑'
    RIGHT = '→'
    DOWN = '↓'
    LEFT = '←'


class SmokeMapper:

    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        # Set map
        with open(self.input, 'r') as f:
            self.map = [self.clean_line(line) for line in f]
        self.max_row = len(self.map) - 1
        self.max_col = len(self.map[0]) - 1

    @staticmethod
    def clean_line(line):
        """Strip line and cast its elements as integer."""
        return [int(digit) for digit in line.rstrip()]

    @staticmethod
    def get_low_points_candidates(line_number, line):
        """Save index and value of points lower than points to their left and right in a line."""
        low_points_candidates = []
        # Check first.
        if line[0] < line[1]:
            low_points_candidates.append(Point(x=line_number, y=0, value=line[0]))

        # Check all points except first and last.
        for index_b, a, b, c in zip(range(1, len(line) - 1), line[:-2], line[1:-1], line[2:]):
            if b < a and b < c:
                low_points_candidates.append(Point(x=line_number, y=index_b, value=b))

        # Check last.
        if line[-1] < line[-2]:
            low_points_candidates.append(Point(x=line_number, y=len(line) - 1, value=line[-1]))

        return low_points_candidates

    def get_low_points(self):
        low_points = []
        with open(self.input, 'r') as f:
            prev_prev_line = None
            prev_line = self.clean_line(next(f))  # Line 0
            for line_number, line in enumerate(f):
                line = self.clean_line(line)
                # Compare the previous line to the one above it and the current line.
                low_points += get_low_points_in_line(line_number=line_number, line=prev_line, prev_line=prev_prev_line, next_line=line)
                prev_prev_line, prev_line = prev_line, line
                # prev_prev = 0 | prev = 1 |
        # Process the last line too.
        low_points += get_low_points_in_line(line_number=line_number + 1, line=prev_line, prev_line=prev_prev_line)
        return low_points

    def part_one(self):
        return get_risk_level(low_points=self.get_low_points())

    def map_basin_recursively(self, basin, x, y, dir=None):
        point = (x, y)
        value = self.map[x][y]
        # Stop if already mapped or if point is of maximum height
        if value == 9 or point in basin:
            return

        # Expand basin
        basin.add(point)
        if x > 0 and dir is not Direction.DOWN:
            self.map_basin_recursively(basin=basin, x=x - 1, y=y, dir=Direction.UP)
        if x < self.max_row and dir is not Direction.UP:
            self.map_basin_recursively(basin=basin, x=x + 1, y=y, dir=Direction.DOWN)
        if y > 0 and dir is not Direction.RIGHT:
            self.map_basin_recursively(basin=basin, x=x, y=y - 1, dir=Direction.LEFT)
        if y < self.max_col and dir is not Direction.LEFT:
            self.map_basin_recursively(basin=basin, x=x, y=y + 1, dir=Direction.RIGHT)

    def part_two(self):
        low_points = self.get_low_points()
        top_3_basins_sizes = [0, 0, 0]
        for point in low_points:
            basin = set()
            self.map_basin_recursively(basin=basin, x=point.x, y=point.y)
            top_3_basins_sizes.append(len(basin))
            top_3_basins_sizes.sort()
            top_3_basins_sizes.pop(0)
        return math.prod(top_3_basins_sizes)


class TestSmokeMapper(TestCase):
    def test_part_one(self):
        self.assertEqual(15, SmokeMapper(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(1134, SmokeMapper(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', SmokeMapper().part_one())
    print('Part Two:', SmokeMapper().part_two())

