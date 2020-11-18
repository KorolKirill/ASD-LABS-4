import time

def quickSort (table, low, high):
	start = time.perf_counter()

	# Когда-то здесь будет код

	end = time.perf_counter()
	finalTime = 1000 * (end - start)
	estimatedTime = "Quick sort for " + str(len(table)) + " elements took " + str(round(finalTime, 3)) + " miliseconds"

	return estimatedTime