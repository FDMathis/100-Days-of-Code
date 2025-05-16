print("Welcome to the tip calculator!")
print()
bill = input("what was the total bill? $")
total_bill = float(bill)
tip_input = input("How much tip would you like to give: 10%, 12%, or 15%?")
tip_percent = int(tip_input) / 100
tip_amt = tip_percent * total_bill
group = input("How many people will split the bill?")
group_size = int(group)

final_bill = ((total_bill + tip_amt) / group_size)

print(f"Each person should pay: ${final_bill:.2f}")



