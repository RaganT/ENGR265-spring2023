import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    a = 1.0
    b = 1.0 / math.sqrt(2.0)
    t = 1.0 / 4.0
    p = 1.0

    for i in range(1, 10):
        a_i = ((a + b) / 2)
        b_i = math.sqrt(a * b)
        t_i = t - (p * ((a - a_i) ** 2))
        p_i = (2 * p)

        pi_iteration = ((a_i + b_i) ** 2) / (4 * t_i)
        abs_error = abs(pi_iteration - math.pi)
        a, b, t, p = a_i, b_i, t_i, p_i
        if abs_error >= target_error:
            continue
        else:
            break

    return pi_iteration


desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned Pi=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
