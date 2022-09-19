age = int(input('How old are you? '))

# if age >= 16 and age <16:
#     print('You can drive, but no social security for you.')

# and requires an agreement to both parts on the condition
# or only requires one condition to be true, both both conditions being true would also satisfy this

# simplifying chained comparisons

if 16 <= age < 65:
    print('You can drive, but no social security for you.')
elif age >= 65:
    print('Congrats on your retirement.')
else:
    print('You\'re too young to drive.')