"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

# in-state total cost, including tuition and room/board costs $30,792
in_state_gift = 30,792

# out-of-state total cost, including tuition and room/board costs $47,882
out_state_gift = 47,882

# if an alumni wanted to just sponsor an in-state student, they would need enough money in their account
# so that their investment yields the total cost for the students, in this case $30,792
test_run = 1000000 * .05
total = (test_run + 1000000)
print(test_run)
print(total)