######### ROLLERCOASTER TICKET MACHINE ###############

print('##### Welcome to Rollercoaster! ########')

height = float(input('What is your height? '))  # user input

if height >= 40:
    print('You can ride the rollercoaster!')    # true if height is more or equal to 40

    age = int(input('What is your age? '))  # user input

    if age <= 12:
        print('You pay $5.00')  # true if age is less or equal to 12
    elif age <= 18:
        print('Please pay $7.00')   # true if age is less or equal to 18
    else:
        print('Please pay $12.00')  # false if age is more than 18
else:
    print('Sorry, you still not tall enough to ride!')  # false if height is less than 40


