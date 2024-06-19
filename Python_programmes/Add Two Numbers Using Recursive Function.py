# Define a recursive function to add two numbers
# def add_numbers_recursive(x, y):
# 	if y == 0:
# 		return x
# 	else:
# 		return add_numbers_recursive(x + 1, y - 1)
#
# # Take input from the user
# num1 = 1
# num2 = 2
#
# # Call the recursive function to add the two numbers
# result = add_numbers_recursive(num1, num2)
#
# # Print the result
# print("The sum of", num1, "and", num2, "is", result)

# -----------------------------------------

#To define a function that take two integers
# and return the sum of those two numbers
# def add(a,b):
# return a+b
#
# #initializing the variables
# num1 = 10
# num2 = 5
#
# #function calling and store the result into sum_of_two numbers
# sum_of_twonumbers = add(num1,num2)
#
# #To print the result
# print("Sum of {0} and {1} is {2};" .format(num1,
# 						num2, sum_of_two numbers))


def evennumbers(num):
	print(num)
	if num==2:
		return(num)
	else:
		return evennumbers(num-2)
evennumbers(8)

