# strings are a sequence data type, a sequence of characters
# you can pick out individual characters or substrings

parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

# characters in strings are indexed starting at zero
print()

# mini challenge: add code to the program to print out "we win", with each letter on a separate line

for i in range(6):
    print('we win'[i])

# index backwards in a string using negative numbers. when counting from the end of the string, start at -1
print()

print(parrot[-1])
print(parrot[-14])

# slicing takes a string and slice it at given start, stop, and step values in the following format [start:stop:step]
# the slice starts at value x and goes up to, but not including, the stop value
print()

print(parrot[0:6])

print(parrot[0:9])
print(parrot[:9])   # if no start given, will default to start of the sequence

# start stop and step values can also be negative

print(parrot[-4:-2])
print(parrot[-4:12])

# the step value defaults to 1

print(parrot[0:6:2])

# negative step values work as well but the start value must be greater than the stop value

print(parrot[14:0:-1])

# stop values are up to, but not including, so how do you get the first letter?
# you must omit the stop value

print(parrot[14::-1])

#challenge
print()

letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[-10:-13:-1])
print(letters[4::-1])
print(letters[-1:-9:-1])

