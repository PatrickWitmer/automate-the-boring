import random
import sys

secret = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20")

for times_guessed in range(1,7):
  print('Take a guess:')

  guess = int(input('>'))
  if guess > secret:
    print('That is to high.')
  elif guess < secret:
    print('That is to low.')
  elif guess == secret:
    print(f"Correct! You're a lizard Larry, the number was {secret}")
    sys.exit()

print(f'To many guesses, the correct number was {secret}')   

