digit_sought = 55
numbers = [2, 4, 5, 9, 10, 15, 55]

def binary_search(sorted_numbers, number_sought):
	low = 0
#With -1 at the end the last number, here 55 would not be found
	high = len(sorted_numbers)
	middle = -1
	while (low < high):
		x = (high + low) / 2
		middle = int(x)
#		print("Middle: " + str(middle))
#		print("Low: " + str(low))
#		print("High: " + str(high))
		if sorted_numbers[middle] == number_sought:
			return sorted_numbers[middle]
		elif sorted_numbers[middle] > number_sought:
			high = middle 
		elif sorted_numbers[middle] < number_sought:
#The following 4 lines solved the problem with the endless loops
			if low == middle:
				low = middle + 1
			else:
				low = middle 
		print ("------")
	print("Number not found")

zahl = binary_search(numbers, digit_sought)
print(zahl)


#for i in range(1, 20):
#	print(binary_search(numbers, i))

