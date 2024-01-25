# Income is $45000
full_income = 45000
print("How much is your income?: $", full_income)
# Tax to pay is %6000
# Lets say we dont know how much tax we need to pay
tax_2pay = 0
# 10000*0% + 10000*10% + 25000*20% = 6000, this is the guide
f_month = 10000
f_tax = 0
s_month = 10000
s_tax = 0.1
t_month = 25000
t_tax = 0.2

if full_income <= f_month:
    tax_2pay = full_income * f_tax
elif full_income <= s_month:
    tax_2pay = f_month * f_tax + (full_income - f_month) * s_tax
else:
    tax_2pay = f_month * f_tax + s_month * s_tax + t_month * t_tax
print("Tax needed to pay is: $", tax_2pay)
