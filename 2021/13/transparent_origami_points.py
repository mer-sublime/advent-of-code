"""https://adventofcode.com/2021/day/13/"""
import re
import textwrap
from enum import Enum
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


class AXIS(Enum):
    X = 'x'
    Y = 'y'


class SYMBOLS(Enum):
    EMPTY = '.'
    DOT = '#'


INSTRUCTION_PATTERN = fr'^fold along ({AXIS.X.value}|{AXIS.Y.value})=(\d+)$'


class FoldInstruction:

    def __init__(self, axis, value):
        self.axis = axis
        self.value = int(value)

    def fold(self, points: set[tuple[int, int]]) -> set[tuple[int, int]]:
        def get_transpose_method() -> callable:
            def transpose_horizontally(x: int, y: int) -> tuple[int, int]:
                return (x, y) if x <= self.value else (2 * self.value - x, y)

            def transpose_vertically(x: int, y: int) -> tuple[int, int]:
                return (x, y) if y <= self.value else (x, 2 * self.value - y)

        new_points = set()
        transpose = get_transpose_method()
        for point in points:
            new_points.add(transpose(*point))
        return new_points


class PointsFolder:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.points = set()
        self.instructions = []
        with open(self.input, 'r') as f:
            # Init points
            while point := next(f).rstrip():
                point = point.split(',')
                self.points.add((int(point[0]), int(point[1])))

            # Parse instructions
            for line in f:
                instruction = re.match(pattern=INSTRUCTION_PATTERN, string=line.rstrip())
                self.instructions.append(FoldInstruction(axis=instruction[1], value=instruction[2]))

    def print_grid(self):
        max_x = max([point[0] for point in self.points])
        max_y = max([point[1] for point in self.points])
        for y in range(max_y + 1):
            row = ''
            for x in range(max_x + 1):
                row += SYMBOLS.DOT.value if (x, y) in self.points else SYMBOLS.EMPTY.value
            print(row)

    def count_dots(self) -> int:
        return len(self.points)

    def part_one(self):
        # Apply only the first fold instruction
        self.points = self.instructions[0].fold(points=self.points)
        return self.count_dots()

    def part_two(self):
        for instruction in self.instructions:
            self.points = instruction.fold(points=self.points)
        return self.count_dots()


class TestPointsFolder(TestCase):
    def test_part_one(self):
        self.assertEqual(17, PointsFolder(test=True).part_one())

    def test_part_one_print(self):
        expected_output = '''
            #.##..#..#.
            #...#......
            ......#...#
            #...#......
            .#.#..#.###
        '''
        folder = PointsFolder(test=True)
        folder.part_one()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            folder.print_grid()
            self.assertEqual(textwrap.dedent(expected_output).strip(), mock_stdout.getvalue().strip())

    def test_print_grid(self):
        expected_grid = '''
            ...#..#..#.
            ....#......
            ...........
            #..........
            ...#....#.#
            ...........
            ...........
            ...........
            ...........
            ...........
            .#....#.##.
            ....#......
            ......#...#
            #..........
            #.#........
        '''
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            PointsFolder(test=True).print_grid()
            self.assertEqual(textwrap.dedent(expected_grid).strip(), mock_stdout.getvalue().strip())

    def test_part_two_print(self):
        expected_grid = '''
            #####
            #...#
            #...#
            #...#
            #####
        '''
        folder = PointsFolder(test=True)
        folder.part_two()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            folder.print_grid()
            self.assertEqual(textwrap.dedent(expected_grid).strip(), mock_stdout.getvalue().strip())


if __name__ == "__main__":
    print('Part One:', PointsFolder().part_one())

    folder = PointsFolder()
    print('Part Two:', folder.part_two())
    folder.print_grid()
