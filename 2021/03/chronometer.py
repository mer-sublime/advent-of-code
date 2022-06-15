#!/usr/bin/env python3
import getopt
import sys
import time
from power_consumption import PowerConsumption

USAGE_MSG = 'usage: chronometer.py [-t <tries>]'


def function_a():
    PowerConsumption().part_one()


def function_b():
    PowerConsumption().part_one_bis()


def parse_arguments(argv):
    try:
        opts, args = getopt.getopt(argv, 'ht:', ['tries='])
    except getopt.GetoptError:
        print(USAGE_MSG)
        sys.exit(2)

    # Determine number of tries
    tries = None
    for opt, arg in opts:
        if opt == '-h':
            print(USAGE_MSG)
            sys.exit()
        elif opt in ("-t", "--tries"):
            tries = int(arg)
            assert tries > 0
            print(f'Number of tries: {tries}')

    if not tries:
        tries = int(input('Number of tries: '))
        assert tries > 0
    return tries


def time_function(func: callable, tries: int):
    start = time.perf_counter()
    for i in range(tries):
        func()
    end_time = time.perf_counter()
    return (end_time - start) / tries


def display_results(a_avg_time, b_avg_time):
    print(f'A: {a_avg_time}s on average.')
    print(f'B: {b_avg_time}s on average.')

    if a_avg_time > 0 and b_avg_time > 0:
        if a_avg_time < b_avg_time:
            fast, slow, ratio = 'A', 'B', 100 * (b_avg_time - a_avg_time) / b_avg_time
        else:
            fast, slow, ratio = 'B', 'A', 100 * (a_avg_time - b_avg_time) / a_avg_time
        if ratio > 0.01:
            print(f'{fast} seems to be {ratio:.2f}% faster than {slow}.')
        else:
            print(f'A and B are about the same in terms of speed.')


def run(tries: int):
    # Time function_a
    a_avg_time = time_function(function_a, tries)

    # Time function_b
    b_avg_time = time_function(function_b, tries)

    display_results(a_avg_time=a_avg_time, b_avg_time=b_avg_time)


if __name__ == '__main__':
    # Retrieve arguments
    tries = parse_arguments(argv=sys.argv[1:])
    run(tries=tries)
