"""https://adventofcode.com/2022/day/2"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'

from enum import Enum


class MultipleEnum(Enum):
    """Custom Enum type that can use multiple values."""
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
    """A Round of Rock Paper Scissor in Part One."""
    class Shape(MultipleEnum):
        ROCK = 1, 'A', 'X'
        PAPER = 2, 'B', 'Y'
        SCISSORS = 3, 'C', 'Z'

    class Outcome(Enum):
        LOSS = 0
        DRAW = 3
        WIN = 6

    def __init__(self, first_shape: str, second_shape: str):
        self.their_shape = self.Shape(first_shape)
        self.my_shape = self.Shape(second_shape)
        self.outcome = self.determine_outcome()

    def determine_outcome(self) -> Outcome:
        """Determine the outcome of the round."""
        win_against = {
            self.Shape.ROCK: self.Shape.SCISSORS,
            self.Shape.PAPER: self.Shape.ROCK,
            self.Shape.SCISSORS: self.Shape.PAPER,
        }
        if self.my_shape == self.their_shape:
            return self.Outcome.DRAW
        if win_against[self.my_shape] == self.their_shape:
            return self.Outcome.WIN
        return self.Outcome.LOSS

    def get_score(self) -> int:
        """Count points awarded for this round."""
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

    def __init__(self, their_shape: str, outcome: str):
        self.their_shape = self.Shape(their_shape)
        self.outcome = self.Outcome(outcome)
        self.my_shape = self.determine_my_shape()

    def determine_my_shape(self) -> Shape:
        """Determine my shape depending of the expected outcome."""
        win_against = {
            self.Shape.ROCK: self.Shape.SCISSORS,
            self.Shape.PAPER: self.Shape.ROCK,
            self.Shape.SCISSORS: self.Shape.PAPER,
        }
        lose_against = {value: key for key, value in win_against.items()}
        match self.outcome:
            case self.Outcome.DRAW:
                return self.their_shape
            case self.Outcome.LOSS:
                return win_against[self.their_shape]
            case self.Outcome.WIN:
                return lose_against[self.their_shape]


class RockPaperScissors:
    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE

    def part_one(self):
        with open(self.input, 'r') as f:
            rounds = [RoundPartOne(*line.split()) for line in f]
        return sum(game.get_score() for game in rounds)

    def part_two(self):
        with open(self.input, 'r') as f:
            rounds = [RoundPartTwo(*line.split()) for line in f]
        return sum(game.get_score() for game in rounds)


class TestRockPaperScissors(TestCase):
    def test_part_one(self):
        self.assertEqual(15, RockPaperScissors(test=True).part_one())

    def test_part_two(self):
        self.assertEqual(12, RockPaperScissors(test=True).part_two())


if __name__ == '__main__':
    print('Part One:', RockPaperScissors().part_one())
    print('Part Two:', RockPaperScissors().part_two())
