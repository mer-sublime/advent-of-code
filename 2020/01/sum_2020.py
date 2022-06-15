def main():
	"""Find the three entries that sum to 2020 and then multiply those numbers together."""
	numbers = []
	with open('input.txt', 'r+') as input_file:
		for number in input_file:
			numbers.append(int(number))
			
	return get_three_terms_of_2020(numbers)


def get_two_terms_of_2020(numbers):
	"""Find the two entries that sum to 2020 and then multiply those numbers together.."""
	for i in numbers:
		for j in numbers:
			if i + j == 2020:
				return i * j


def get_three_terms_of_2020(numbers):
	"""Find the three entries that sum to 2020 and then multiply those numbers together."""
	for i in numbers:
		for j in numbers:
			for k in numbers:
				if i + j + k == 2020:
					return i * j * k


if __name__ == "__main__":
	main()
