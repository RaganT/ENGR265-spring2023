"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""


# compounding interest formula: final = principal * ((1 + (rate / 100)) ** n)

# I will start off by calculating the 10-year investment first
# this is his initial money he invested
principal_10 = 44000000000
# this is the rate of interest he would get on a 10-year investment
rate_10 = 3.96
# this is how many years the investment is held for
n_10 = 10
ten_year = (principal_10 * ((1 + (rate_10 / 100)) ** n_10))
print(float("%.2f"%ten_year))

# Second, I will calculate the 20-year investment
# this is his initial money he invested
principal_20 = 44000000000
# this is the rate of interest he would get on a 20-year investment
rate_20 = 4.32
# this is how many years the investment is held for
n_20 = 20
twenty_year = (principal_20 * ((1 + (rate_20 / 100)) ** n_20))
print(float("%.2f"%twenty_year))

# In conclusion, here are the final values that Elon Musk would yield in 10- and 20-year investments
# final answer for 10-year
ten_year_final = print("Ten year final amount is $" , float("%.2f"%ten_year))

# final answer for 20-year
twenty_year_final = print("Twenty year final amount is $" , float("%.2f"%twenty_year))
