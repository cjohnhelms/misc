answer = 5

print('Please guess a number between 1 and 10:')
guess = int(input())

# if guess < answer:
#     print('Too low, enter a second guess:')
#     guess = int(input())
#     if guess == answer:
#         print('Correct')
#     else:
#         print('Sorry, incorrect')
# elif guess > answer:
#     print('Too high, enter a second guess:')
#     guess = int(input())
#     if guess == answer:
#         print('Correct')
#     else:
#         print('Sorry, incorrect')
# else:
#     print('You guessed correctly on the first try')

##############################################################################################

# same thing, but more efficient

# if guess != answer:
#     if guess < answer:
#         print('Too low, please guess higher')
#     else:
#         print('Too high, please guess lower')
#     guess = int(input())
#     if guess == answer:
#         print('Congratulations, that is correct.')
#     else:
#         print('Sorry, that is incorrect.')
# else:
#     print('Congratulations, you guessed correctly on the first try.')

###############################################################################################

# infinite guesses, instead of just 2

if guess != answer:
    while guess != answer:
        if guess < answer:
            print('Too low, please guess higher')
        else:
            print('Too high, please guess lower')
        guess = int(input())
        if guess == answer:
            print('Congratulations, you are correct.')
else:
    print('Congratulations, you guessed correctly on the first try.')