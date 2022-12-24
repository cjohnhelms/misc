# program that prints out the integers from 1 to 100, except we're going to replace integers with words when they're multiples of three multiples or five, or if they're multiples of both three and five.

for num in range(1,101):
    if (num % 3) == 0 and (num % 5) == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)