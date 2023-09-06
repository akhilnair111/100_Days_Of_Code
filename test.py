# print("Hello World!!")
# print(1_2 + 1_0)

# aa = int(input("Enter two digit no: \n"))
# print(type(aa))
# print(aa[0] + aa[1])

age = int(input("What is your age"))
max_days = 90 * 365
max_weeks = 90 * 52
max_months = 90 * 12

age_to_days = age * 365
age_to_weeks = age * 52
age_to_months = age * 12

print(f"You have {max_days - age_to_days} days, {max_weeks - age_to_weeks} weeks, and  {max_months - age_to_months} months left.")
