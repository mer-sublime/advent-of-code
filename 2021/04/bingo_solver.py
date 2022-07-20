"""https://adventofcode.com/2021/day/"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'

CHECKED = 'X'
LENGTH = 5
WINNING_LINE = [CHECKED] * LENGTH


class BingoBoard:
    rows = []

    def __init__(self, rows):
        self.rows = rows

    def check_rows(self):
        return WINNING_LINE in self.rows

    def check_cols(self):
        self.cols = [[row[index] for row in self.rows] for index in range(LENGTH)]
        return WINNING_LINE in self.cols

    def check_victory(self):
        return self.check_rows() or self.check_cols()

    def get_score(self):
        return self.winning_number * sum([sum([int(cell) for cell in row if cell is not CHECKED]) for row in self.rows])

    def play_number(self, number):
        for index, row in enumerate(self.rows):
            if number in row:
                self.rows[index] = [CHECKED if cell == number else cell for cell in row]

    def set_winning_number(self, number):
        self.winning_number = int(number)

    def __repr__(self):
        return ' \n'.join('\t'.join(row) for row in self.rows)


class BingoSolver:
    boards = []

    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.init_boards()

    def init_boards(self):
        with open(self.input, 'r') as f:
            # Get instructions
            self.instructions = next(f).split(',')

            # Get boards
            self.boards = []
            board = []
            for line in f:
                if line := line.split():
                    board.append(line)
                elif board:  # New bingo board
                    self.boards.append(BingoBoard(board))
                    board = []
            # Save last board
            self.boards.append(BingoBoard(board))

    def play(self):
        for number in self.instructions:
            for board in self.boards:
                board.play_number(number=number)
                if board.check_victory():
                    board.set_winning_number(number=number)
                    return board.get_score()
        return False

    def print_boards(self):
        print(f'INSTRUCTIONS: {self.instructions}')
        for index, board in enumerate(self.boards):
            print(f'BOARD {index}:\n{board}\n')


class BingoSolverTwo(BingoSolver):

    def play(self):
        for number in self.instructions:
            for board in self.boards[:]:
                board.play_number(number=number)
                if board.check_victory():
                    board.set_winning_number(number=number)
                    self.boards.remove(board)
        return board.get_score()


class TestPuzzle(TestCase):
    def test_part_one(self):
        self.assertEqual(4512, BingoSolver(test=True).play())

    def test_part_two(self):
        self.assertEqual(1924, BingoSolverTwo(test=True).play())


if __name__ == "__main__":
    print('Part One:', BingoSolver().play())
    print('Part Two:', BingoSolverTwo().play())
