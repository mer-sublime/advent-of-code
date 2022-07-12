"""https://adventofcode.com/2021/day/5"""
import unittest
from enum import Enum

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class Direction(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    DIAGONAL = 'diagonal'


class Point:
    x, y, coordinates = (None,) * 3

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.coordinates = (self.x, self.y)

    def __repr__(self):
        return f'({self.x},{self.y})'


class Line:
    start, end, direction = (None,) * 3

    def __init__(self, text):
        coordinates = text.split(' -> ')
        self.start = Point(*coordinates[0].split(','))
        self.end = Point(*coordinates[1].split(','))

    def get_points(self):
        if self.start.x == self.end.x:
            self.direction = Direction.HORIZONTAL
            if self.start.y > self.end.y:
                self.start, self.end = self.end, self.start
            return [(self.start.x, y) for y in range(self.start.y, self.end.y + 1)]
        elif self.start.y == self.end.y:
            self.direction = Direction.VERTICAL
            if self.start.x > self.end.x:
                self.start, self.end = self.end, self.start
            return [(x, self.start.y) for x in range(self.start.x, self.end.x + 1)]

    def __repr__(self):
        return f'{self.start} -> {self.end}'


class LinePartTwo(Line):

    def get_points(self):
        if points := super().get_points():    # The line is horizontal or vertical, return result.
            return points

        # Else, the line is diagonal.
        self.direction = Direction.DIAGONAL 

        x_sign = 1 if self.start.x < self.end.x else -1
        y_sign = 1 if self.start.y < self.end.y else -1

        # return [(self.start.x + step * x_sign, self.start.y + step * x_sign) for step in range(abs(self.start.x - self.end.x) + 1)]

        points = []
        for step in range(abs(self.start.x - self.end.x) + 1):
            x = self.start.x + x_sign * step
            y = self.start.y + y_sign * step
            points.append((x, y))
        return points


class VentMapper:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def map_vents(self, line_class):
        points = []

        with open(self.input, 'r') as f:
            for row in f:
                line = line_class(row)
                if line_points := line.get_points():
                    points += line_points

        counter = dict.fromkeys(set(points), 0)
        for point in points:
            counter[point] += 1

        return sum([1 for point, count in counter.items() if count >= 2])

    def part_one(self):
        return self.map_vents(line_class=Line)

    def part_two(self):
        return self.map_vents(line_class=LinePartTwo)


class TestVentMapper(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(VentMapper(test=True).part_one(), 5)

    def test_part_two(self):
        self.assertEqual(VentMapper(test=True).part_two(), 12)


if __name__ == "__main__":
    print('Part One:', VentMapper().part_one())
    print('Part Two:', VentMapper().part_two())

