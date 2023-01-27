"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.
"""

# in-state total cost, including tuition and room/board costs $30,792
in_state_tuition = 30792

# out-of-state total cost, including tuition and room/board costs $47,882
out_state_tuition = 47882

# interest rate
rate = 5/100

in_state_gift = (in_state_tuition/rate)
print(in_state_gift)

out_state_gift = (out_state_tuition/rate)
print(out_state_gift)

in_state_investment = (in_state_gift + in_state_tuition)
print(in_state_investment)

out_state_investment = (out_state_gift + out_state_tuition)
print(out_state_investment)