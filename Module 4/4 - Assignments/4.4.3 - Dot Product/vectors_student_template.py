import random
import numpy as np


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)

    # return the generated list
    return randoms


"""
Step 1: Generate two "vectors" of equal length but full of random values
"""
max_length = 10
maximum_value = 100
fixed_length = int(random.uniform(2, max_length))
vector_a = generate_random_int_list(fixed_length, maximum_value)
vector_b = generate_random_int_list(fixed_length, maximum_value)
print(vector_b)
print(vector_a)

"""
Step 2: Iterate through the vector(s) and calculate the dot product
"""

# store your result here. Do not change the name
dot_product = 0

# the dot product takes the nth element of first vector and multiplies it by the nth element of the other vector

for n in range(0, len(vector_a)) and range(0, len(vector_b)):
    a = vector_a[n]
    b = vector_b[n]
    dpt = (a * b)
    dot_product = dot_product + dpt


"""
Step 3: Calculate the error of your dot_product compared with numpy's solution
"""
# check code with numpy...
a_np = np.asarray(vector_a)
b_np = np.asarray(vector_b)

# use dot product from numpy to check this result
correct = np.dot(a_np, b_np)
error = correct - dot_product

# compare results
print("Your result: ", dot_product)
print("Correct result: ", correct)
print("Error: ", error)
