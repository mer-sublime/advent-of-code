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

    def _merge_lists(self, list_a, list_b):
        return [[
            '#' if char_a != char_b else char_a for char_a, char_b in zip(row_a, row_b)
        ] for row_a, row_b in zip(list_a, list_b)]

    def fold(self, grid: list[list], debug=False) -> list[list]:
        if debug:
            print(f'Folding along {self.axis}={self.value}')

        match self.axis:
            case AXIS.X.value:
                return self.fold_vertically(grid=grid)
            case AXIS.Y.value:
                return self.fold_horizontally(grid=grid)

    def fold_vertically(self, grid: list[list]) -> list[list]:
        return self.fold_horizontally(grid=list(zip(*grid)))

    def fold_horizontally(self, grid: list[list]) -> list[list]:
        # @TODO: Simplify this
        grid_top = grid[:self.value]
        grid_bottom = grid[self.value + 1:]
        merged_grid = list(zip(reversed(grid_top), grid_bottom))
        merged_grid.reverse()
        return [
            ['#' if char_a != char_b else char_a for char_a, char_b in zip(row_a, row_b)]
            for row_a, row_b in merged_grid]
#        return self._merge_lists(grid_top, grid_bottom_reversed)


class PaperFolder:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.max_row, self.max_col = 0, 0
        self.grid, self.points, self.instructions = [], [], []
        with open(self.input, 'r') as f:
            # Init points
            while point := next(f).strip():
                point = point.split(',')
                self.points.append((int(point[0]), int(point[1])))

            # Parse instructions
            for line in f:
                instruction = re.match(pattern=INSTRUCTION_PATTERN, string=line.strip())
                self.instructions.append(FoldInstruction(axis=instruction[1], value=instruction[2]))

        # Init grid
        self.init_grid()

    def init_grid(self):
        # Create empty grid
        self.max_row = max((point[0] for point in self.points))
        self.max_col = max((point[1] for point in self.points))
        self.grid = [
            [SYMBOLS.EMPTY.value for y in range(self.max_row + 1)]
            for x in range(self.max_col + 1)
        ]
        # Mark dots
        for point in self.points:
            self.grid[point[1]][point[0]] = SYMBOLS.DOT.value

    def print_grid(self):
        for row in self.grid:
            print(''.join(row))

    def count_dots(self) -> int:
        if not self.grid:
            return 0

        return sum(row.count(SYMBOLS.DOT.value) for row in self.grid)

    def part_one(self):
        # Apply only the first fold instruction
        self.grid = self.instructions[0].fold(self.grid)

        return self.count_dots()

    def part_two(self):
        pass


class TestPaperFolder(TestCase):
    def test_part_one(self):
        self.assertEqual(17, PaperFolder(test=True).part_one())

    def test_part_one_print(self):
        expected_output = '''
            #.##..#..#.
            #...#......
            ......#...#
            #...#......
            .#.#..#.###
            ...........
            ...........
        '''
        folder = PaperFolder(test=True)
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
            PaperFolder(test=True).print_grid()
            self.assertEqual(textwrap.dedent(expected_grid).strip(), mock_stdout.getvalue().strip())

    def test_part_two(self):
        self.assertEqual(True, PaperFolder(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', PaperFolder().part_one())
    # print('Part Two:', PaperFolder().part_two())
