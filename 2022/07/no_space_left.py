"""https://adventofcode.com/2022/day/07"""
from unittest import TestCase
from typing import Optional, Union

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'
ROOT_DIR = '/'
PARENT_DIR = '..'
SIZE_LIMIT = 100000


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"] = None):
        self.name = name
        self.parent = parent
        self.children = dict()

    def add_child(self, child: Union['Directory', 'File']) -> None:
        self.children[child.name] = child

    def get_sub_directories(self):
        return {name: subdir for name, subdir in self.children.items() if isinstance(subdir, self.__class__)}

    def get_sub_directory(self, name):
        try:
            return self.get_sub_directories()[name]
        except KeyError:
            raise KeyError(f"No Directory named '{name }' in {self.name}.")

    @property
    def size(self) -> int:
        return sum(child.size for child in self.children.values())

    def __repr__(self):
        return f'{self.name}: (dir, size={self.size})'


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name}: (file, size={self.size})'


class SpaceSaver:

    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.current_dir = None
        self.root = Directory(name=ROOT_DIR, parent=None)

    def parse_input(self):
        with open(self.input, 'r') as f:
            for line in f:
                line = line.strip()
                match line:
                    case line if line == '$ ls':
                        continue
                    case line if line.startswith('$ cd'):
                        self.parse_cd(line=line)
                    case line if line.startswith('dir'):
                        self.parse_dir_info(line=line)
                    case _:
                        self.parse_file_info(line=line)

    def parse_cd(self, line: str):
        destination = line.split()[2]
        if destination == ROOT_DIR:
            self.current_dir = self.root
        elif destination == PARENT_DIR:
            self.current_dir = self.current_dir.parent
        else:
            self.current_dir = self.current_dir.get_sub_directory(name=destination)

    def parse_dir_info(self, line: str):
        self.current_dir.add_child(Directory(name=line.split()[1], parent=self.current_dir))

    def parse_file_info(self, line: str):
        size, name = line.split()
        self.current_dir.add_child(File(name=name, size=int(size)))

    def sum_subdir_sizes_under_limit(self, directory: Directory) -> int:
        if not directory.get_sub_directories():
            return directory.size

        total_sizes = directory.size if directory.size <= SIZE_LIMIT else 0
        for sub_directory in directory.get_sub_directories().values():
            if (sub_size := self.sum_subdir_sizes_under_limit(directory=sub_directory)) <= SIZE_LIMIT:
                total_sizes += sub_size
        return total_sizes

    def part_one(self):
        # @TODO: Answer was too low!
        self.parse_input()
        result = self.sum_subdir_sizes_under_limit(directory=self.root)
        return result

    def part_two(self):
        pass


class TestSpaceSaver(TestCase):
    def test_part_one(self):
        self.assertEqual(95437, SpaceSaver(test=True).part_one())

    # def test_part_two(self):
    #     self.assertEqual(True, SpaceSaver(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', SpaceSaver().part_one())
    # print('Part Two:', SpaceSaver().part_two())
