# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    random_vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return random_vars


"""
Given a random list of integers, return two lists of only even and odd values from that random list
"""
# generate two random lists of integers
max_length = 20
upper_bound = 100
nums = generate_random_int_list(max_length, upper_bound)

# lists to hold the even and odd numbers
# do not modify their names
evens_list = []
odds_list = []

for n in nums:
    if (n % 2 == 0):
       # print("Value is Even")
        num_evens_new = list()
        num_evens_new.append(n)


    else:
       # print("Value is Odd")
        num_odds_new = list()
        num_odds_new.append(n)

print("The evens list contains: ", evens_list)
print("The odds list contains: ", odds_list)

