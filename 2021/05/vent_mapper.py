"""https://adventofcode.com/2021/day/"""
from enum import Enum
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class Direction(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


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


class VentMapper:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def part_one(self):
        points = []

        with open(self.input, 'r') as f:
            for row in f:
                line = Line(row)
                if line_points := line.get_points():
                    points += line_points

        counter = dict.fromkeys(set(points), 0)
        for point in points:
            counter[point] += 1
        return sum([1 for point, count in counter.items() if count >= 2])

    def part_two(self):
        with open(self.input, 'r') as f:
            for line in f:
                pass


class TestVentMapper(TestCase):
    def test_part_one(self):
        self.assertEqual(VentMapper(test=True).part_one(), 5)

    # def test_part_two(self):
    #     self.assertEqual(VentMapper(test=True).part_two(), True)


if __name__ == "__main__":
    print('Part One:', VentMapper().part_one())
#   print('Part Two:', VentMapper().part_two())
