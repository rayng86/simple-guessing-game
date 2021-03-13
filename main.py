#! /usr/bin/python3
import random

computer_guess = random.randint(0,101)

stored_guesses = [0]
guess_within_10_below = computer_guess - 10
guess_within_10_above = computer_guess + 10
while True:
    my_input = input("Guess a number between 1 and 100. ")
    try:
        my_guess = int(my_input)
        
        # keep track of previous guesses
        stored_guesses.append(my_guess)
        
        # if guess is less than 1 or higher than 100, return out of bounds msg
        if my_guess < 1 or my_guess > 100:
            print('You are OUT OF BOUNDS!')
            continue
            
        # if guess is correct, print and stop while loop
        if my_guess == computer_guess:
            print(f'you guessed correctly. It took you {len(stored_guesses)-1} tries.')
            break
            
        if my_guess in range(computer_guess, guess_within_10_above) or my_guess in range(guess_within_10_below, computer_guess):
            if stored_guesses[-2] and abs(my_guess-computer_guess) < abs(stored_guesses[-2]-computer_guess):
                print('WARMER')
            else:
                print('WARM')
        else:
            if stored_guesses[-2]:
                print('COLDER')
            else:
                print('COLD')
    except ValueError:
        print('please guess a number only')
