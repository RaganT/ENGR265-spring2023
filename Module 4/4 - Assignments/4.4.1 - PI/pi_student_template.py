import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1.0
b = 1.0/math.sqrt(2.0)
t = 1.0/4.0
p = 1.0

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """
    # this is where the Gauss-Legendre algorithm equation goes
    a_i = ((a + b) / 2)
    b_i = math.sqrt(a * b)
    t_i = t - (p * ((a - a_i) ** 2))
    p_i = (2 * p)

    pi_iteration = ((a_i + b_i) ** 2) / (4 * t_i)
    # a, b, t, p = a_i, b_i, t_i, p_i
    a = a_i
    b = b_i
    t = t_i
    p = p_i

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i, ",", pi_iteration)


"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = pi_iteration

print("Final estimate for PI: ", pi_estimate)
print(abs(pi_estimate - math.pi))
print("Error on estimate: ", abs(pi_estimate - math.pi))
