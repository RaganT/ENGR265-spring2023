"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
import numpy as np

# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

random_list_A_std = np.std(random_list_A)
random_list_B_std = np.std(random_list_B)

# set this variable equal to the list with the largest standard deviation
# do not modify this variable's name, you can/should adjust the contents ;)
# e.g. longest_list_is = myList


if random_list_A_std > random_list_B_std:
    print("Random list A has a bigger standard deviation")
    new_list = random_list_A

if random_list_B_std > random_list_A_std:
    print("Random list A has a bigger standard deviation")
    new_list = random_list_B

longest_list_is = new_list
