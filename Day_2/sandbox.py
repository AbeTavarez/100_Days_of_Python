##### SINGLE NUMBER ADDER ###################

two_digit_number = input('Please enter a two digit number: ')   # user input

first_digit = int(two_digit_number[0])  # grabs the first char and convert it to an int

second_digit = int(two_digit_number[1]) # grabs the second char and convert it to an int

sum = first_digit + second_digit

print(f'The sum of {two_digit_number} is {sum}')