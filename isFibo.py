test_cases = int(raw_input())

fibo = [0, 1]
number = []

def check(number):
	if (number in fibo):
		return "isFibo"
	else:
		return "isNotFibo"

for x in range(1, test_cases+1):
	number.append(int(raw_input()))

for digit in number:
	while fibo[-1] <= digit:
		fibo.append(fibo[-1] + fibo[-2])
	print check(digit)

		

	





	