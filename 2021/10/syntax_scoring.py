"""https://adventofcode.com/2021/day/10"""
from unittest import TestCase
from collections import deque

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'


CHARACTER_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


class SyntaxScoring:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    @staticmethod
    def get_syntax_error_score(character):
        match character:
            case ')':
                return 3
            case ']':
                return 57
            case '}':
                return 1197
            case '>':
                return 25137
            case _:
                return 0

    def part_one(self):
        with open(self.input, 'r') as f:
            syntax_error_score = 0
            for line in f:
                expected_closing_chars = deque()
                for c in line:
                    if c in CHARACTER_PAIRS:
                        expected_closing_chars.append(CHARACTER_PAIRS[c])
                    elif c != expected_closing_chars.pop():
                        syntax_error_score += self.get_syntax_error_score(c)
                        break
            return syntax_error_score

    def part_two(self):
        with open(self.input, 'r') as f:
            for line in f:
                pass


class TestSyntaxScoring(TestCase):
    def test_part_one(self):
        self.assertEqual(26397, SyntaxScoring(test=True).part_one())

    # def test_part_two(self):
    #     self.assertEqual(True, SyntaxScoring(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', SyntaxScoring().part_one())
    # print('Part Two:', SyntaxScoring().part_two())
