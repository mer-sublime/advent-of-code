import re


def main():
    """Find how many passwords are valid according to their policy."""
    valid_passwords = 0
    with open('input.txt', 'r+') as input_file:
        for line in input_file:
            if validate_second_policy(line):
                valid_passwords += 1
    return valid_passwords


def validate_first_policy(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line, re.U)
    if m:
        character = m.group(3)
        password = m.group(4)
        count = password.count(character)
        return int(m.group(1)) <= count <= int(m.group(2))
    return False


def validate_second_policy(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line, re.U)
    if m:
        first_position = int(m.group(1)) - 1
        second_position = int(m.group(2)) - 1
        character = m.group(3)
        password = m.group(4)
        return (password[first_position] == character) ^ (password[second_position] == character)
    return False


if __name__ == "__main__":
    print(main())
