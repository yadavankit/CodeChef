test_cases = int(raw_input())

input_collection = []
result = []

def fruit_transaction(fruits):
	if (int(fruits[0]) == int(fruits[1])):
		return fruits
	minimum = min(fruits) 
	maximum = max(fruits)
	arranged = [minimum, maximum]
	return arranged

for x in range(1, test_cases + 1):
	input_collection.append(raw_input().split())

for input_set in input_collection:
	while(input_set[2] > 0):
		fruits = [int(input_set[0]), int(input_set[1])]
		new_set = fruit_transaction(fruits)
		input_set[2] = int(input_set[2]) - 1
		input_set[0] = int(new_set[0])
		input_set[1] = int(new_set[1])
		input_set[0] = int(input_set[0]) + 1
	print(abs(int(input_set[1]) - int(input_set[0])))


