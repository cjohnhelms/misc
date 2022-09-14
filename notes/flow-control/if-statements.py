name = input('Please enter your name: ')
age = int(input('How old are you {0}? '.format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote.")
#     print('Please put an X in the box.')
# else:
#     print('Please come back in {0} years.'.format(18 - age))

# statements in python are denoted by a : which starts a new code block

print()

# elif example

if age < 18:
    print('Please come back in {0} years.'.format(18 - age))
elif age == 900:
    print('You should be dead by now.')
else:
    print("You are old enough to vote.")
    print('Please put an X in the box.')

# if blocks
# when testing for equality, make sure to use == and not =
# an if statement can includ many elif parts, but only one else
# the else must come after all elifs