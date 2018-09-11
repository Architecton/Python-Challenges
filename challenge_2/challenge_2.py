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
	raw_in = input()
	# TODO

######################################################################################################

# Command handlers ###################################################################################
def addition():
	print("Addition")

def subtraction():
	print("Subtraction")

def multiplication():
	print("Multiplication")

def division():
	print("Division")

def pru():
	print("Principal root of unity")
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
		commands.get(next_line)()
	# if entered blank line (only the '\n' character), exit program.
	elif next_line == "":
		pass
	else:
		print("Unrecognized command. Please try again.")

#########################################################################################################