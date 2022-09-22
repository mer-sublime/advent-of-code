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

    @staticmethod
    def autocomplete_line(line):
        expected_closing_chars = deque()
        for c in line:
            if c in CHARACTER_PAIRS:
                expected_closing_chars.appendleft(CHARACTER_PAIRS[c])
            elif c != expected_closing_chars.popleft():
                return
        return ''.join(expected_closing_chars)

    @staticmethod
    def get_completion_score(completion_string):
        score = 0
        for character in completion_string:
            score *= 5
            match character:
                case ')':
                    score += 1
                case ']':
                    score += 2
                case '}':
                    score += 3
                case '>':
                    score += 4
                case _:
                    score += 0
        return score

    def part_two(self):
        with open(self.input, 'r') as f:
            scores = []
            for line in f:
                completion_string = self.autocomplete_line(line.rstrip())
                if completion_string:
                    scores.append(self.get_completion_score(completion_string=completion_string))
            return sorted(scores)[len(scores) // 2]


class TestSyntaxScoring(TestCase):
    def test_part_one(self):
        self.assertEqual(26397, SyntaxScoring(test=True).part_one())

    def test_autocomplete_line(self):
        self.assertEqual('}}]])})]', SyntaxScoring.autocomplete_line(line='[({(<(())[]>[[{[]{<()<>>'))
        self.assertEqual(')}>]})', SyntaxScoring.autocomplete_line(line='[(()[<>])]({[<{<<[]>>('))
        self.assertEqual('}}>}>))))', SyntaxScoring.autocomplete_line(line='(((({<>}<{<{<>}{[]{[]{}'))
        self.assertEqual(']]}}]}]}>', SyntaxScoring.autocomplete_line(line='{<[[]]>}<{[{[{[]{()[[[]'))
        self.assertEqual('])}>', SyntaxScoring.autocomplete_line(line='<{([{{}}[<[[[<>{}]]]>[]]'))

    def test_get_completion_score(self):
        self.assertEqual(288957, SyntaxScoring.get_completion_score(completion_string='}}]])})]'))
        self.assertEqual(5566, SyntaxScoring.get_completion_score(completion_string=')}>]})'))
        self.assertEqual(1480781, SyntaxScoring.get_completion_score(completion_string='}}>}>))))'))
        self.assertEqual(995444, SyntaxScoring.get_completion_score(completion_string=']]}}]}]}>'))
        self.assertEqual(294, SyntaxScoring.get_completion_score(completion_string='])}>'))

    def test_part_two(self):
        self.assertEqual(288957, SyntaxScoring(test=True).part_two())


if __name__ == "__main__":
    print('Part One:', SyntaxScoring().part_one())
    print('Part Two:', SyntaxScoring().part_two())
