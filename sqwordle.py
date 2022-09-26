import random
from unittest import result
from termcolor import colored

pokemonFile = open('./pokemon.txt')
pokemonStr = pokemonFile.read()
pokemonList = pokemonStr.split(", ")

# defining the variables

secret = random.choice(pokemonList)
spaces = 'X' * len(secret)
guessNum = 0

# intro statement for the game and poviding the length of the answer

print('This is Sqwordle, the Wordle for Pokemon. You have 6 guesses. If you don\'t know how this works, please go play Wordle first.')
print(spaces + ' - ' + str(len(secret)))

# taking the first guess

def take_guess():
    g = str(input().title())
    while len(g) != len(secret) or g not in pokemonList:
        print('Please enter a guess of ' + str(len(secret)) + ' characters from 1st generation Pokemon.')
        g = str(input().title())
    return g
guess = take_guess()
    
# main body of the game

while guess != secret:
    if guessNum <=4:
        for i in range(len(secret)):
            spaces = list(spaces)
            if guess[i] == secret[i]:
                spaces[i] = colored(guess[i], 'green')
            elif guess[i] in secret:
                spaces[i] = colored(guess[i], 'blue')
            else:
                spaces[i] = colored(guess[i], 'red')
        result = ''.join(spaces)
        print(result)
        guessNum += 1
        guess = take_guess()
    else:
        print('Sorry, better luck next time.')
        exit()
else:
    print('Congratulations!')
