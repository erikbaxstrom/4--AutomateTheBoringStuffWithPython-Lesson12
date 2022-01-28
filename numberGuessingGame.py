import random
import sys

# ask for users name
print('What is your name?')
name = input()
# validate? nah

# pick a random number from 1-20
number = random.randint(1,20)
print('Hello,', name, 'I am thinking of a number between 1 and 20')


# ask for guesses
for i in range(0,6): 
    print('Take a guess')
    try:
        guess = int(input())
    except:
        print('hmm. that does not seem to be a number.')
        continue # go back to start of loop to ask for another guess
    # compare guess to number
    if guess > number:     # if high, tell
        print('too high')
        continue # go back to start of loop to ask for another guess
    elif guess < number:# if just right, finish
        print('too low')
        continue # go back to start of loop to ask for another guess
    else: # if just right, finish
        print('Good job! It took you', i, 'guesses.')
        sys.exit()

# if too many guesses, you failed
print('Nope. The number was', number)
