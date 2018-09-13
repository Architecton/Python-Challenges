# Implement a calculator for working with complex numbers. It should support addition, subtraction, multiplication, division and computing the n-th primitive root of unity.

# Define the following functions:

 # add        // adding complex numbers
 # multiply   // multiplying complex numbers
 # multiply   // multiplying complex numbers with real numbers
 # divide     // division of complex numbers
 # n_root     // computing the n-th primitive root of unity

# The calculator should support the commands:

# + (addition),
# - (subtraction),
# * (multiplication),
# / (division),
# w (printing the n-th primitive root and all its powers).
# in case of command +, -, *, / parse two complex numbers after the command. In case of the command w, parse an integer n. The execution of the program should stop when entering a blank line.
# The results should be rounded to 5 decimal places.
#####################################################################################################

# define variable that holds line entered by used. Initialize with initial value.
next_line = " "

# Parsing complex numbers from user input ############################################################
def parse_num():
	while True:
		raw_in = input() 						# Read raw user input.
		trimmed_in = raw_in.replace(" ", "") 	# Remove spaces.
		# Check if real part starts with a sign
		if trimmed_in[0] == "+" or trimmed_in[0] == "-":
			# Extract values of real and imaginary parts.
			re_start = 0
			im_start = trimmed_in[1:].find("+") + 1

			# If plus not found, look for minus.
			if im_start == 0:
				im_start = trimmed_in[1:].find("-") + 1

			# Extract.
			re = trimmed_in[re_start:im_start]
			im = trimmed_in[im_start:-1]

			# Construct and return complex number.
			# Check for validity of input.
			try:
				result = complex(float(re), float(im)) 
				return complex(float(re), float(im))
			except ValueError:
				print("Could not parse number. Please try again.")
				return parse_num()

		else:
			# Extract values of real and imaginary parts.
			re_start = 0
			im_start = trimmed_in[1:].find("+") + 1

			# If plus not found, look for minus.
			if im_start == 0:
				im_start = trimmed_in[1:].find("-") + 1

			# Extract.
			re = trimmed_in[re_start:im_start]
			im = trimmed_in[im_start:-1]

			# Construct and return complex number.
			# Check for validity of input.
			try:
				result = complex(float(re), float(im)) 
				return complex(float(re), float(im))
			except ValueError:
				print("Could not parse number. Please try again.")
				

######################################################################################################

# Parsing the argument for the nth principal root of unity functionality #############################
def parse_n():
	while True:
		raw_in = input()
		trimmed_in = raw_in.replace(" ", "")
		try:
			res = int(trimmed_in)
			return res
		except ValueError:
			print("Invalid input. Please try again.")

######################################################################################################

# Command handlers ###################################################################################
# addition
def addition():
	# Parse the two complex numbers.
	num1 = parse_num()
	num2 = parse_num()
	# Compute and return result.
	return num1 + num2

# subtraction
def subtraction():
	# Parse the two complex numbers.
	num1 = parse_num()
	num2 = parse_num()
	# Compute and return result.
	return num1 - num2

# multiplication
def multiplication():
	# Parse the two complex numbers.
	num1 = parse_num()
	num2 = parse_num()
	# Compute and return result.
	return num1 * num2

# division
def division():
	# Parse the two complex numbers.
	num1 = parse_num()
	num2 = parse_num()
	# Compute and return result.
	return num1 / num2

# powers of principal root of unity
from math import sin, cos, pi
def pru():
	
	# Parse n (Which root of unity and its powers to compute and print)
	n = parse_n()

	# Go over valid powers.
	for k in range(1, n + 1):

		# Compute the real and imaginary parts of the complex numbers.
		re = cos((k/n)*2*pi);
		im = sin((k/n)*2*pi);

		# Check if any part below threshold.
		if abs(im) < 1e-6:
			im = 0
		

		if abs(re) < 1e-6:
			re = 0
		
		# Construct complex number.
		res = complex(round(re, 5), round(im, 5));

		# Handle rounding errors.
		if abs(im) > 0.000009:
			# Get sign of complex part (used for printing).
			sign_im = "-" if im < 0 else "+"
			# Print according to sign of imaginary part.
			if sign_im == "+":
				print(str(res.real) + "+" + str(res.imag) + "i", end = '')
			else:
				print(str(res.real) + str(res.imag) + "i", end = '')
		else:
			print(res.real, end = '')
		
		# If another power follows, separate with space
		if k < n:
			print(" ", end = '');
		else:
			print()

#######################################################################################################

# Define a dictionary that maps valid commands to handling functions.
commands = {"+" : addition, "-" : subtraction, "*" : multiplication, "/" : division, "w" : pru}

# Main loop ############################################################################################
while(next_line != ""):
	# Read and parse command from user input.
	next_line = input("Enter command (+, -, *, /, w):\n")
	next_line.strip()

	# Check if entered line represents a valid command.
	if next_line in commands.keys():
		# Except for the principal root of unity functionality, get and print result.
		if next_line != "w":
			res = commands.get(next_line)()
			# Get sign of imaginary part (used for printing).
			sign_im = "-" if res.imag < 0 else "+"
			# Print result according to sign of imaginary part.
			if sign_im == "+":
				print(str(res.real) + "+" + str(res.imag) + "i")
			else:
				print(str(res.real) + str(res.imag) + "i")
		else:
			commands.get(next_line)()

	# if entered blank line (only the '\n' character), exit program.
	elif next_line == "":
		pass
	else:
		print("Unrecognized command. Please try again.")

#########################################################################################################