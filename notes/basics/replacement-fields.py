# what if you want to print both ints and strs in one print call
# one approach is to use the str function. every data type can be coerced into an str representation

age = 24
print('my age is ' + str(age) + ' years')

# this can become tedious. python 3 allows for replacement fields in the .format method

print('my age is {0} years'.format(age))