import random
from unittest import result
from termcolor import colored

# def takeGuess():
#     guess = str(input().title())
#     while len(guess) != len(secret):
#         print('Please enter a guess of ' + str(len(secret)) + ' characters.')
#         guess = str(input().title())

pokemonFile = open('pokemon.txt')
pokemonStr = pokemonFile.read()
pokemonList = pokemonStr.split(", ")


secret = random.choice(pokemonList)
spaces = 'X' * len(secret)

print('This is Sqwordle, the Wordle for Pokemon. You have 6 guesses. If you don\'t know how this works, please go play Wordle first.')
print(spaces + '-' + str(len(secret)))
print(secret)
guess = str(input().title())
while len(guess) != len(secret):
        print('Please enter a guess of ' + str(len(secret)) + ' characters.')
        guess = str(input().title())
guessNum = 0
    
while guess != secret:
    if guessNum <=4:
        for i in range(len(secret)):
            spaces = list(spaces)
            if guess[i] == secret[i]:
                spaces[i] = colored(guess[i], 'green')
            elif guess[i] in secret:
                spaces[i] = colored(guess[i], 'yellow')
            else:
                spaces[i] = colored(guess[i], 'red')
        result = ''.join(spaces)
        print(result)
        guessNum += 1
        guess = str(input().title())
        while len(guess) != len(secret):
            print('Please enter a guess of ' + str(len(secret)) + ' characters.')
            guess = str(input().title())
    else:
        print('Sorry, better luck next time.')
        exit()
else:
    print('Congratulations!')
