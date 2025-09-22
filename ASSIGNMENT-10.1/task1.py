def calc_average(marks):
	if not marks:
		return 0  # Return 0 if the list is empty to avoid division by zero
	total = 0
	for m in marks:
		total += m
	average = total / len(marks)
	return average  # Fixed typo

marks = [85, 90, 78, 92]
print("Average Score is ", calc_average(marks))
