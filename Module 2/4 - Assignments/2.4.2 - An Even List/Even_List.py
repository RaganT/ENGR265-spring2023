import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

# use len() to find the length of the list
list_length = len(even_list)
print(list_length)

# now calculate the first middle index of the list
middle_index_1 = (list_length//2) -1
print(middle_index_1)
middle_element_1 = even_list[middle_index_1]
print(middle_element_1)

# calculate the second middle index of the list
middle_index_2 = (list_length//2)
print(middle_index_2)
middle_element_2 = even_list[middle_index_2]
print(middle_element_2)

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = (middle_element_1 + middle_element_2) / 2

# the average of middle elements is
print("The average is: ", middle_average)
