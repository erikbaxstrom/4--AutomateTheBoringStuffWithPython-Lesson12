import random

# ask for users name
print('What is your name?')
name = input()
# validate? nah

# pick a random number from 1-20
number = random.randint(1,20)
print('Hello,', name, 'I am thinking of a number between 1 and 20')

guess = '' # start with empty string for edge case where user inputs only garbage

# ask for guesses
for guessCount in range(1,7): # I forgot that it tells you i at the end, so this should be (1,7) instead of (0,6)
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
#        sys.exit() # unnecessary. Just break out of the for loop and then check if number == guess
        break
if guess == number: # if they're the same, you guessed correctly
    print('Good job', name + '! It took you', guessCount, 'guesses.') # this is how Al did it in the video. I'm very surprised that the counter guessCount is available after the for loop terminates. Also, print('string', int + 'string) works, but seems sketchy
else: # if too many guesses, you failed
    print('Nope. The number was', number)
