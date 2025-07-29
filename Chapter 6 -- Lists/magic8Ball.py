import random

# We need to remake the magic 8 ball program but using lists.

magicBallAnswers = [
  'It is certain',
  'It is decidedly so',
  'Yes',
  'Reply hazy try again',
  'Ask again later',
  'Concentrate and ask again',
  'My reply is no',
  'Outlook not so good',
  'Very doubtful',
]

print('Ask the balls a question:')
question = input('>')

# These are tests prints so I can understand the length of the list, and why we use -1 in the random (it's 9 strings long, but we need a random number for the index of 0-8)
# print(len(magicBallAnswers))
# print(magicBallAnswers[8])

print(magicBallAnswers[random.randint(0, len(magicBallAnswers) - 1)])


