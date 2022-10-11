"""https://adventofcode.com/2021/day/11"""
from pprint import pprint
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'

STEPS = 100
ROWS = 10
COLS = 10


class DumboOctopus:
    def __init__(self, grid, x, y, energy):
        self.grid, self.x, self.y, self.energy = grid, x, y, energy
        self.has_flashed = False
        self.nearby_octopuses = []

    def get_nearby_octopuses(self):
        if not self.nearby_octopuses:
            min_row = self.x - 1 if self.x > 0 else 0
            max_row = self.x + 1 if self.x + 1 < ROWS else self.x
            min_col = self.y - 1 if self.y > 0 else 0
            max_col = self.y + 1 if self.y + 1 < COLS else self.y
            for row in range(min_row, max_row + 1):
                for col in range(min_col, max_col + 1):
                    if not (row == self.x and col == self.y):
                        self.nearby_octopuses.append(self.grid[row][col])
        return self.nearby_octopuses

    def flash(self):
        self.energy = 0
        self.has_flashed = True
        flash_counter = 1
        # Increase energy of nearby octopuses
        nearby_octopuses = self.get_nearby_octopuses()
        for octopus in nearby_octopuses:
            flash_counter += octopus.incr_energy()
        return flash_counter

    def incr_energy(self):
        if not self.has_flashed:
            self.energy += 1
            if self.energy > 9:
                return self.flash()
        return 0

    def __repr__(self):
        if self.has_flashed:
            return f'*{self.energy}*'
        return str(self.energy)


class FlashForecaster:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.grid = [[0] * COLS for _ in range(ROWS)]
        self.flash_counter = 0
        with open(self.input, 'r') as f:
            for row, line in enumerate(f):
                for col, digit in enumerate(line.rstrip()):
                    self.grid[row][col] = DumboOctopus(grid=self.grid, x=row, y=col, energy=int(digit))
        print('Before any steps:')
        self.print_grid()

    def reset_flash_flags(self):
        for line in self.grid:
            for octopus in line:
                octopus.has_flashed = False

    def do_step(self):
        for line in self.grid:
            for octopus in line:
                self.flash_counter += octopus.incr_energy()
        self.reset_flash_flags()

    def part_one(self):
        for step in range(1, STEPS + 1):
            self.do_step()
            print(f'\n After step {step}:')
            self.print_grid()
        return self.flash_counter

    def part_two(self):
        pass

    def print_grid(self):
        pprint(self.grid)


class TestFlashForecaster(TestCase):
    def test_part_one(self):
        self.assertEqual(1656, FlashForecaster(test=True).part_one())

    # def test_part_two(self):
    #     self.assertEqual(True, FlashForecaster(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', FlashForecaster().part_one())
    # print('Part Two:', FlashForecaster().part_two())
