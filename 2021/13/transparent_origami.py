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

    def fold(self, grid: list[list], debug=False) -> list[list]:
        if debug:
            print(f'Folding along {self.axis}={self.value}')

        match self.axis:
            case AXIS.X.value:
                return self.fold_vertically(grid=grid)
            case AXIS.Y.value:
                return self.fold_horizontally(grid=grid)

    def fold_vertically(self, grid: list[list]) -> list[list]:
        # Flip the grid
        flipped_grid = list(zip(*grid))
        # Fold the flipped grid
        folded_grid = self.fold_horizontally(grid=flipped_grid)
        # Flip the folden grid back
        return list(zip(*folded_grid))

    def fold_horizontally(self, grid: list[list]) -> list[list]:
        def merge_lines(line_a: list[str], line_b: list[str]) -> list[str]:
            """Merge two lines in one."""
            def merge_chars(a: str, b: str) -> str:
                """Return the DOT symbol if there is at least one and the EMPTY symbol otherwise."""
                return SYMBOLS.DOT.value if SYMBOLS.DOT.value in (a, b) else SYMBOLS.EMPTY.value

            return [merge_chars(a, b) for a, b in zip(line_a, line_b)]

        top_half = grid[:self.value]
        bottom_half = grid[self.value + 1:]
        return [merge_lines(line_a, line_b) for line_a, line_b in zip(top_half, reversed(bottom_half))]


class PaperFolder:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.max_row, self.max_col = 0, 0
        self.grid, self.instructions, points = [], [], []
        with open(self.input, 'r') as f:
            # Init points
            while point := next(f).rstrip():
                point = point.split(',')
                points.append((int(point[0]), int(point[1])))

            # Parse instructions
            for line in f:
                instruction = re.match(pattern=INSTRUCTION_PATTERN, string=line.rstrip())
                self.instructions.append(FoldInstruction(axis=instruction[1], value=instruction[2]))

        # Init grid
        self.init_grid(points=points)

    def init_grid(self, points):
        # Create empty grid
        self.max_row = max((point[0] for point in points))
        self.max_col = max((point[1] for point in points))
        grid = [
            [SYMBOLS.EMPTY.value for y in range(self.max_row + 1)]
            for x in range(self.max_col + 1)
        ]
        # Mark dots
        for point in points:
            grid[point[1]][point[0]] = SYMBOLS.DOT.value

        # Cast rows into strings
        self.grid = grid

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
        for instruction in self.instructions:
            self.grid = instruction.fold(self.grid)
        return self.count_dots()


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

    def test_part_two_print(self):
        expected_grid = '''
            #####
            #...#
            #...#
            #...#
            #####
            .....
            .....
        '''
        folder = PaperFolder(test=True)
        folder.part_two()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            folder.print_grid()
            self.assertEqual(textwrap.dedent(expected_grid).strip(), mock_stdout.getvalue().strip())


if __name__ == "__main__":
    print('Part One:', PaperFolder().part_one())

    folder = PaperFolder()
    print('Part Two:', folder.part_two())
    folder.print_grid()
