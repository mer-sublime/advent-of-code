"""https://adventofcode.com/2022/day/6"""
from unittest import TestCase

INPUT_FILE = 'input.txt'
TEST_INPUT_FILES_FORMAT = 'test_input_{}.txt'
START_OF_PACKET_MARKER_SIZE = 4
START_OF_MESSAGE_MARKER_SIZE = 14


class SignalLocker:
    """Lock signal of the elves handled device."""
    def __init__(self, marker_size, input_file=INPUT_FILE):
        self.marker_size = marker_size
        self.input = input_file

    def is_marker(self, buffer: str) -> bool:
        """Return if the buffer correspond to a marker."""
        return len(set(buffer)) == self.marker_size

    def lock_signal(self) -> int:
        """Return number of characters to process before the marker is detected."""
        with open(self.input, 'r') as f:
            line = f.read().rstrip()
        i = 0
        j = self.marker_size
        while not self.is_marker(buffer=line[i:j]):
            i += 1
            j = i + self.marker_size
        return j


class TestSignalLocker(TestCase):
    def test_part_one(self):
        expected_results = [7, 5, 6, 10, 11]
        for index, result in enumerate(expected_results):
            self.assertEqual(result, SignalLocker(
                marker_size=START_OF_PACKET_MARKER_SIZE,
                input_file=TEST_INPUT_FILES_FORMAT.format(index + 1)).lock_signal())

    def test_part_two(self):
        expected_results = [19, 23, 23, 29, 26]
        for index, result in enumerate(expected_results):
            self.assertEqual(result, SignalLocker(
                marker_size=START_OF_MESSAGE_MARKER_SIZE,
                input_file=TEST_INPUT_FILES_FORMAT.format(index + 1)).lock_signal())


if __name__ == '__main__':
    print('Part One:', SignalLocker(marker_size=START_OF_PACKET_MARKER_SIZE).lock_signal())
    print('Part Two:', SignalLocker(marker_size=START_OF_MESSAGE_MARKER_SIZE).lock_signal())
