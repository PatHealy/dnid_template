# hello_world.py
# 1/13/25

# This file reviews a few basic data structure operations you should be somewhat familiar with, 
#	with a focus on lists and dictionaries.

# Its exercises are oriented around functions. If you aren't too familiar with how functions 
#	work in Python or would like some kind of refresher, 
#	please consult this tutorial: https://www.w3schools.com/python/python_functions.asp 

# Exercises begin on line 33

############################################################
# HELPER FUNCTIONS
############################################################

#this is a helper function to format our tests later:
def format_test(input_example, your_code, expected_result):
	#Did you know Python code can have emojis? It can!
	result = "⛔TEST FAILED (" + str(input_example) + ")"
	if your_code == expected_result:
		return "👍TEST SUCCEEDED (" + str(input_example) + ")"
	result = result + "\n\tYour code returned: " + str(your_code) + "\n\tExpected: " + str(expected_result) 
	return result

def print_test(input_example, your_code, expected_result):
	print(format_test(input_example, your_code, expected_result))

############################################################
# EXERCISES START
############################################################

# EXERCISE 1: How many 5's?
# Write a function that takes in a list of numbers as a parameter and returns the number of 5's in the list.
def count_fives(data):
	#YOUR WORK HERE
	pass

#These tests should all pass if you wrote count_fives correctly
print("==========\nTESTING EXERCISE 1\n==========")
data1 = [1,2,3,4,5]
data2 = [5, 5, 5, 4]
data3 = [5, -5, 2, 10, 10, 15]
data4 = []
data5 = data1 + data2 + data3 + data4

print_test(data1, count_fives(data1), 1)
print_test(data2, count_fives(data2), 3)
print_test(data3, count_fives(data3), 1)
print_test(data4, count_fives(data4), 0)
print_test(data5, count_fives(data5), 5)


#EXERCISE 2: Oops all fives
# Write a function that takes in any list of numbers and returns a list of the same length except every element is the number 5.
#	A challenge that might be fun to review: do it with a list comprehension and it'll be a one-line function!
def oops_all_fives(data):
	#YOUR WORK HERE
	pass

print("==========\nTESTING EXERCISE 2\n==========")
datasets = [data1, data2, data3, data4, data5]
for dataset in datasets:
	print_test(dataset, count_fives(oops_all_fives(dataset)), len(dataset))

# EXERCISE 3: Number Counting Dictionary
# Repeat exercise 1 but this time let's make it much more generalizable. This time we'll count EVERY number.
# The method will take in a list of numbers and return a dictionary of the frequencies of every unique number.

# FOR EXAMPLE, say we are given the input: [1, 1, 4, 2, 1, 2]
#	We should return the dictionary: {1: 3, 2: 2, 4: 1}
#	That dictionary indicates that there are three 1's in the list, two 2's, and one 4.
def count_everything(data):
	#YOUR WORK HERE
	pass

print("==========\nTESTING EXERCISE 3\n==========")
data6 = [1, 1, 4, 2, 1, 2]
print_test(data6, count_everything(data6), {1: 3, 2: 2, 4: 1})
print_test(data1, count_everything(data1), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
print_test(data2, count_everything(data2), {5: 3, 4: 1})
print_test(data3, count_everything(data3), {5: 1, -5: 1, 2: 1, 10: 2, 15: 1})
print_test(data4, count_everything(data4), {})
print_test(data5, count_everything(data5), {1: 1, 2: 2, 3: 1, 4: 2, 5: 5, -5: 1, 10: 2, 15: 1})
