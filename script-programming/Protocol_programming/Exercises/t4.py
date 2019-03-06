def largest(numbers):
	largest = numbers[0]
	for x in numbers:
		if x > largest:
			largest = x
	return largest

a = [2,4,76,545,657]

print largest(a)
