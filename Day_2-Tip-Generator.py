print("Welcome to the tip calculator")

total_bill= float(input("What was the total bill? $"))
tip= int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split_between= int(input("How many people would split this bill? "))

formula= (total_bill+(tip/100)*total_bill)/split_between
per_person_bill= round(formula, 2)

print(f"Each person should pay ${per_person_bill}")