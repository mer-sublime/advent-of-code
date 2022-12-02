"""https://adventofcode.com/2022/day/2"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'

from enum import Enum


class MultipleEnum(Enum):
    def __new__(cls, *values):
        obj = object.__new__(cls)
        # first value is canonical value
        obj._value_ = values[0]
        for other_value in values[1:]:
            cls._value2member_map_[other_value] = obj
        obj._all_values = values
        return obj

    def __repr__(self):
        return '<%s.%s: %s>' % (
            self.__class__.__name__,
            self._name_,
            ', '.join([repr(v) for v in self._all_values]),)


class RoundPartOne:
    class Shape(MultipleEnum):
        ROCK = 1, 'A', 'X'
        PAPER = 2, 'B', 'Y'
        SCISSORS = 3, 'C', 'Z'

    class Outcome(Enum):
        LOSS = 0
        DRAW = 3
        WIN = 6

    win_against = {
        Shape.ROCK: Shape.SCISSORS,
        Shape.PAPER: Shape.ROCK,
        Shape.SCISSORS: Shape.PAPER,
    }

    my_shape = None
    their_shape = None

    def __init__(self, first_shape: str, second_shape: str):
        self.their_shape = self.Shape(first_shape)
        self.my_shape = self.Shape(second_shape)
        # Determine outcome
        if self.my_shape == self.their_shape:
            self.outcome = self.Outcome.DRAW
        elif self.win_against[self.my_shape] == self.their_shape:
            self.outcome = self.Outcome.WIN
        else:
            self.outcome = self.Outcome.LOSS

    def get_score(self) -> int:
        return self.my_shape.value + self.outcome.value


class RoundPartTwo(RoundPartOne):
    class Shape(MultipleEnum):
        ROCK = 1, 'A'
        PAPER = 2, 'B'
        SCISSORS = 3, 'C'

    class Outcome(MultipleEnum):
        LOSS = 0, 'X'
        DRAW = 3, 'Y'
        WIN = 6, 'Z'

    win_against = {
        Shape.ROCK: Shape.SCISSORS,
        Shape.PAPER: Shape.ROCK,
        Shape.SCISSORS: Shape.PAPER,
    }
    lose_against = {value: key for key, value in win_against.items()}

    def __init__(self, their_shape: str, outcome: str):
        self.their_shape = self.Shape(their_shape)
        self.outcome = self.Outcome(outcome)
        # Determine my shape
        match self.outcome:
            case self.Outcome.DRAW:
                self.my_shape = self.their_shape
            case self.Outcome.LOSS:
                self.my_shape = self.win_against[self.their_shape]
            case self.Outcome.WIN:
                self.my_shape = self.lose_against[self.their_shape]


class RockPaperScissors:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def part_one(self):
        with open(self.input, 'r') as f:
            rounds = [RoundPartOne(*line.split()) for line in f]
        return sum(round.get_score() for round in rounds)

    def part_two(self):
        with open(self.input, 'r') as f:
            rounds = [RoundPartTwo(*line.split()) for line in f]
        return sum(round.get_score() for round in rounds)


class TestRockPaperScissors(TestCase):
    def test_part_one(self):
        self.assertEqual(15, RockPaperScissors(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(12, RockPaperScissors(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', RockPaperScissors().part_one())
    print('Part Two:', RockPaperScissors().part_two())
