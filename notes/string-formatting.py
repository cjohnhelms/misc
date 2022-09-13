for i in range(1,13):
    print('no. {0} squared is {1} and cubed is {2}'.format(i, i ** 2, i ** 3))

# you can include multiple replacements with the .format option, as well as expressions.
# the replacement fields are notated by {x} and the corresponding value is notated in the () following the .format, delimited by a comma

# add field width formatting with a :x after the replacement field value

print()
for i in range(1,13):
    print('no. {0:2} squared is {1:3} and cubed is {2:4}'.format(i, i ** 2, i ** 3))

# to left align, add a less than

print()

for i in range(1,13):
    print('no. {0:2} squared is {1:<3} and cubed is {2:<4}'.format(i, i ** 2, i ** 3))

# to center, use a ^
# specify floating point precision using a decimal point after the width
print()

print('pi is approximately {0:12}'.format(22/7))
print('pi is approximately {0:12f}'.format(22/7))
print('pi is approximately {0:12.50f}'.format(22/7))

# if the precision is greater than the width, pyton will ignore the width