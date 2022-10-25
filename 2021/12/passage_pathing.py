"""https://adventofcode.com/2021/day/"""
from enum import Enum
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE_1 = 'test_input_1.txt'
TEST_INPUT_FILE_2 = 'test_input_2.txt'
TEST_INPUT_FILE_3 = 'test_input_3.txt'

START_NAME = 'start'
END_NAME = 'end'


class Cave:
    class TYPES(Enum):
        BIG = 1
        SMALL = 2

    def __init__(self, name):
        self.name = name
        self.network = set()

    def get_type(self):
        if self.name.isupper():
            return self.TYPES.BIG
        return self.TYPES.SMALL

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(repr(self))


class PathFinder:
    def __init__(self, input_file=INPUT_FILE):
        self.input = input_file
        self.caves = {}
        self.paths = set()
        self.init_caves()

    def init_caves(self):
        with open(self.input, 'r') as f:
            for line in f:
                name_a, name_b = line.rstrip().split('-')
                # Get or create new caves
                cave_a = self.caves.get(name_a, Cave(name=name_a))
                cave_b = self.caves.get(name_b, Cave(name=name_b))
                cave_a.network.add(cave_b)
                cave_b.network.add(cave_a)
                self.caves[name_a] = cave_a
                self.caves[name_b] = cave_b
        # self.print_caves()

    def print_caves(self):
        for cave in self.caves.values():
            print(f'{cave.name}: {cave.network}')

    def explore(self, cave, path):
        # Add current cave to path
        path.append(cave)
        # Save path and exit if we reached the end
        if cave.name == END_NAME:
            self.paths.add('-'.join(node.name for node in path))
            return
        # Explore all neighbours
        for neighbour in cave.network:
            neighbour_type = neighbour.get_type()
            if neighbour_type is Cave.TYPES.BIG or neighbour not in path:
                self.explore(cave=neighbour, path=path.copy())

    def part_one(self):
        self.explore(cave=self.caves[START_NAME], path=[])
        return len(self.paths)

    def part_two(self):
        pass


class TestPathFinder(TestCase):
    def test_part_one_1(self):
        self.assertEqual(10, PathFinder(input_file=TEST_INPUT_FILE_1).part_one())

    def test_part_one_2(self):
        self.assertEqual(19, PathFinder(input_file=TEST_INPUT_FILE_2).part_one())

    def test_part_one_3(self):
        self.assertEqual(226, PathFinder(input_file=TEST_INPUT_FILE_3).part_one())

    # def test_part_two(self):
    #     self.assertEqual(True, PathFinder(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', PathFinder().part_one())
    # print('Part Two:', Puzzle().part_two())
