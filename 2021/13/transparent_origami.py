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


class PaperFolder:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.max_row, self.max_col = 0, 0
        self.grid, self.points, self.instructions = [], [], []
        instruction_pattern = fr'^fold along ({AXIS.X.value}|{AXIS.Y.value})=(\d+)$'
        with open(self.input, 'r') as f:
            # Init points
            while point := next(f).strip():
                point = point.split(',')
                self.points.append((int(point[0]), int(point[1])))

            # Parse instructions
            for line in f:
                instruction = re.match(pattern=instruction_pattern, string=line.strip())
                self.instructions.append({instruction[1]: instruction[2]})

        # Init grid
        self.init_grid()

    def init_grid(self):
        # Create empty grid
        self.max_row = max((point[0] for point in self.points))
        self.max_col = max((point[1] for point in self.points))
        self.grid = [
            ['.' for y in range(self.max_row + 1)]
            for x in range(self.max_col + 1)
        ]
        # Mark dots
        for point in self.points:
            self.grid[point[1]][point[0]] = '#'

    def print_grid(self):
        print()
        for row in self.grid:
            print(''.join(row))

    def fold_grid(self, axis, axis_value):
        pass

    def part_one(self):
        self.print_grid()
        return 17

    def part_two(self):
        pass


class TestPaperFolder(TestCase):
    def test_part_one(self):
        self.assertEqual(17, PaperFolder(test=True).part_one())

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
            PaperFolder(test=True).print_grid()
            self.assertEqual(textwrap.dedent(expected_grid), mock_stdout.getvalue())

    def test_part_two(self):
        self.assertEqual(True, PaperFolder(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', PaperFolder().part_one())
    # print('Part Two:', PaperFolder().part_two())
