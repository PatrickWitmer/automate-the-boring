import random

def magicBalls(balls_number):
  if balls_number == 1:
    return 'It is certain'
  elif balls_number == 2:
    return 'It is decidedly so'
  elif balls_number == 3:
    return 'Yes'
  elif balls_number == 4:
    return 'Reply hazy try again'
  elif balls_number == 5:
    return 'Ask again later'
  elif balls_number == 6:
    return 'Concentrate and ask again'
  elif balls_number == 7:
    return 'My reply is no'
  elif balls_number == 8:
    return 'Outlook not so good'
  elif balls_number == 9:
    return 'Very doubtful'

print('Ask the balls a question:')
question = input('>')

print(magicBalls(random.randint(1,9)))