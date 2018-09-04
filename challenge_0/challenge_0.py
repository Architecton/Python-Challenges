# Write a program that empirically compares two search algorithms for
# sorted arrays:
#	- linear search
#	- binary search
#
# Run both algorithms multiple times for different array sizes and measure
# the average running time.

# Imports
import random
import time
import matplotlib.pyplot as plt

# Define a function that that generates test cases.
def generate_list(n):
	return list(range(1, n + 1))

# Define a function that performs linear search for element el on the passed list.
def linear_search(el, lst):
	for i in range(len(lst)):
		if lst[i] == el:
			return i
	return -1

# Define a function that performs binary search for element el on passed list.
def binary_search(el, lst):
	# Define auxiliary function that takes additional parameters.
	def binary_search_aux(el, lst, l, r):
		if r >= l:
			mid = l + (r - l)//2 		# Compute middle index of table.
			if lst[mid] == el: 		# If found element, return index.
				return mid
			if lst[mid] > el: 			# Else search in appropriate half.
				return binary_search_aux(el, lst, l, mid - 1)
			else:
				return binary_search_aux(el, lst, mid + 1, r)
		return -1
	# Call auxiliary function
	return binary_search_aux(el, lst, 0, len(lst) - 1)

# Define a function that takes initial list length, incrementation step, number of repetitions and search function
# and returns a matrix where the first column contains the table length and the second column contains the run time.
def get_times(starting_length, step, num_steps, num_reps, search_func):
	measurements = ()

	# Make time measurements for various lenghts of lists.
	for n in range(starting_length, starting_length + num_steps * step, step):

		# Generate a list of length n.
		lst = generate_list(n)

		# Start timer.
		start_time = time.perf_counter_ns()

		# Perform the algorithm num_reps times.
		for rep in range(num_reps):
			to_find = random.randint(1, len(lst))
			search_func(to_find, lst)

		# Stop timer.
		end_time = time.perf_counter_ns()

		# Compute average run time for a single search.
		avg_runtime = (end_time - start_time) / num_reps

		# Add to matrix of measurements.
		measurement = (n, avg_runtime / 1e6)
		measurements = measurements + (measurement,)

	# Return matrix of measurements.
	return measurements

# Call function with initial list length of 1000, and using 100 incrementations by 1000. Run the algorithm 1000 times for each length
# and get matrix of measurements.
linear_search_times = get_times(1000, 1000, 10, 1000, linear_search)
binary_search_times = get_times(1000, 1000, 10, 1000, binary_search)

# Extract data for plotting.
n_linear = [i[0] for i in linear_search_times]
n_binary = [i[0] for i in binary_search_times]

t_linear = [i[1] for i in linear_search_times]
t_binary = [i[1] for i in binary_search_times]

# Plot data.
plt.plot(n_linear, t_linear, '-b', label='Linear Search')
plt.plot(n_binary, t_binary, '-r', label='Binary Search')
plt.legend(loc='upper left')
plt.title('Linear Search and Binary Search Comparison')
plt.xlabel('List Length')
plt.ylabel('Run Time')
plt.show()