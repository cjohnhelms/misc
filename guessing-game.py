answer = 5

print('Please guess a number between 1 and 10:')
guess = int(input())

if guess < answer:
    print('Too low, enter a second guess:')
    guess = int(input())
    if guess == answer:
        print('Correct')
    else:
        print('Sorry, incorrect')
elif guess > answer:
    print('Too high, enter a second guess:')
    guess = int(input())
    if guess == answer:
        print('Correct')
    else:
        print('Sorry, incorrect')
else:
    print('You guessed correctly on the first try')