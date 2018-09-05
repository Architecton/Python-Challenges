# Implement two algorithms that search for both the minimum and the maximum element in the list at the same time.
# Implement the search using:
#	- an iterative algorithm,
#	- a recursive algorithm (divide and conquer algorithm)
#
# Empirically compare run times for each algorithm for increasing list lengths.

# imports
from random import randint, choices
import time
import matplotlib.pyplot as plt

# Generate_list: generate a list of random integers on [lower_bound, upper_bound] of length n.
def generate_list(lower_bound, upper_bound, n):
	return choices(range(lower_bound, upper_bound + 1), k = n)

# linear_minmax: implementation of a linear search for the minimum and maximum values.
def linear_minmax(l):
	minimum = l[0] 				# Assume first element to be minimum and maximum.
	maximum = l[0]
	for e in l:					# Go over elements in list and compare to current minimum and maximum.
		if e > maximum:
			maximum = e
		if e < minimum:
			minimum = e

	return {"minimum" : minimum, "maximum" : maximum} 	# Return found minimum and maximum

# dc_minmax: implementation of minimum and maximum search using a divide and conquer algorithm.
def dc_minmax(l):
	# Define an auxiliary function with additional parameters used for recursion.
	def dc_minmax_aux(l, left, right):
		if abs(left - right) <= 1: 										# Base case: if list is of length 1 or 2
			if left == right: 											# if list is of length 1 -> element is both min and max.
				min_max = l[left]
				return {"minimum" : min_max, "maximum" : min_max}
			else:
				return {"minimum" : min(l[left], l[right]), "maximum" : max(l[left], l[right])} # If list of length 2, compare in a trivial fashion.
		else:
			midpoint = (right + left) // 2 														# Compute midle element index in the list.
			result_left = dc_minmax_aux(l, left, midpoint) 										# Find minimum and maximum of left sublist.
			result_right = dc_minmax_aux(l, midpoint + 1, right) 								# Find minimum and maximum of right sublist.
			
			# Find minimum of minimums and maximum of maximums.
			return{"minimum" : min(result_left.get("minimum"), result_right.get("minimum")), "maximum" : max(result_left.get("maximum"), result_right.get("maximum"))} 	

	# Call auxiliary function.
	return dc_minmax_aux(l, 0, len(l) - 1)


def get_times(starting_length, step, num_steps, num_reps, search_func):
	measurements = ()

	for n in range(starting_length, starting_length + step * num_steps, step):
		time_acc = 0
		# Run algorithm num_reps times
		for rep in range(num_reps):
			# Generate list.
			test_list = generate_list(-int(1e3), int(1e3), n)
			# Start timer.
			start_time = time.perf_counter_ns()
			# Run algorithm.
			search_func(test_list)
			# End timer.
			end_time = time.perf_counter_ns()
			# Add measurements to accumulator.
			time_acc += end_time - start_time

		# Get average time.
		avg_runtime = time_acc / num_reps

		# Add measurement to matrix of measurements.
		measurement = (n, avg_runtime / 1e6)
		measurements = measurements + (measurement,)

	return measurements

# Perform tests
linear_measurements = get_times(1000, 1000, 100, 1, linear_minmax)
dc_measurements = get_times(1000, 1000, 100, 1, dc_minmax)

# Extract data for plotting.
n_linear = [i[0] for i in linear_measurements]
n_dc = [i[0] for i in dc_measurements]

t_linear = [i[1] for i in linear_measurements]
t_dc = [i[1] for i in dc_measurements]

# Plot data.
plt.plot(n_linear, t_linear, '-b', label='Linear Search')
plt.plot(n_dc, t_dc, '-r', label='Divide and Conquer Search')
plt.legend(loc='upper left')
plt.title('Linear Search and Divide and Conquer Minimum/Maximum Search Comparison')
plt.xlabel('List Length')
plt.ylabel('Run Time')
plt.show()