print("Welcome to the tip calculator")
total_bill = input("what was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
no_of_ppl = input("How many people to split the bill? ")

int_total_bill = float(total_bill)
int_tip_percentage = int(tip_percentage)
int_no_of_ppl = int(no_of_ppl)

percent_total = int_total_bill + (int_total_bill * (int_tip_percentage / 100))
split_percent = percent_total / int_no_of_ppl
round_split_percent = round(split_percent,2)
print(f"Each person should pay: ${round_split_percent}")