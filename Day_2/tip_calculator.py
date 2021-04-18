####### TIP CALCULATOR #############

print('Welcome to the Tip Calculator')

bill = int(input('What is the total bill? '))   # user input

tip_percentage = int(input('What percentage tip would you like to give? 10, 15 or 20 '))    # user input

bill_split = int(input('How many people to split the bill? '))  # user input

tip_percentage_float = tip_percentage / 100 # get the float number of the tip percentage

calculated_percentage = bill * tip_percentage_float # the dollar amount to tip

final_bill = calculated_percentage + bill   # total with bill and percentage

final_bill_split = final_bill / bill_split  # splits bill by the number of people

print(f'The bill is {bill}')
print(f'The total bill with a {tip_percentage}% tip is {final_bill}')
print(f'Each person should pay {final_bill_split}')

