"""https://adventofcode.com/2021/day/6"""
from unittest import TestCase
from unittest.mock import patch

INPUT_FILE = 'input.txt'
TEST_INPUT_FILE = 'test_input.txt'
NEW_FISH_TIMER = 8
RESET_FISH_TIMER = 6


class LanternFishCounter:

    def __init__(self, test=False):
        self.input = TEST_INPUT_FILE if test else INPUT_FILE
        self.fishes = [0] * (NEW_FISH_TIMER + 1)

    def pass_time(self, days=80):
        with open(self.input, 'r') as f:
            for fish in list(map(int, f.readline().split(','))):
                self.fishes[fish] += 1

        print(f'Initial state: {self.count_fishes()} fishes.\t {self.fishes}')

        for day in range(days):
            new_fishes = self.fishes[0]
            for i in range(NEW_FISH_TIMER):
                self.fishes[i] = self.fishes[i + 1]         # Decrement timer of all fishes.
            self.fishes[RESET_FISH_TIMER] += new_fishes     # Reset 0-day timers to 6.
            self.fishes[NEW_FISH_TIMER] = new_fishes        # Add newborn fishes.

        count = self.count_fishes()
        print(f'After {days} days: {count} fishes.\t {self.fishes}\n')
        return count

    def count_fishes(self):
        return sum(self.fishes)


class TestLanternFishCounter(TestCase):
    def test_pass_time(self):
        self.assertEqual(LanternFishCounter(test=True).pass_time(days=18), 26)
        self.assertEqual(LanternFishCounter(test=True).pass_time(days=80), 5934)
        self.assertEqual(LanternFishCounter(test=True).pass_time(days=256), 26984457539)


if __name__ == "__main__":
    print('Count:', LanternFishCounter().pass_time(days=256))
