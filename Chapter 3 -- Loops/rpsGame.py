import random, sys

print('ROCK < PAPER < SCiSSORS')

wins = 0
losses = 0 
ties = 0

while True: # Main game loop
  print(f'{wins} Wins, {losses} Losses, {ties} Ties')

  while True: # Player loop
    print('Enter your move: (r)ock (p)aper) (s)cissors or (q)uit')
    player_move = input('>')
    if player_move == 'q':
      sys.exit()
    if player_move == 'r' or player_move == 'p' or player_move == 's':
      break # Break out of the player input loop
    print('Please type one of r, p, s, q')

  # Display what the player picked
  if player_move == 'r':
    players_pick = 'Rock'
  elif player_move == 'p':
    players_pick = 'Paper'
  elif player_move == 's':
    players_pick = 'Scissors'

  print(f'{players_pick} versus...')

  # Display what the Computer picked
  computer_number = random.randint(1,3)
  if computer_number == 1:
    computers_pick = "Rock"
  elif computer_number == 2:
    computers_pick = "Paper"
  elif computer_number == 3:
    computers_pick = "Scissors"

  print(f'{computers_pick}')

  # Who wins and display win/lose/tie counts
  if players_pick == computers_pick:
    print('It is a tie!')
    ties += 1     
  elif players_pick == "Rock" and computers_pick == "Scissors":
    print('You win!')
    wins += 1
  elif players_pick == "Paper" and computers_pick == "Rock":
    print('You win!')
    wins += 1
  elif players_pick == "Scissors" and computers_pick == "Paper":
    print('You win!')
    wins += 1
  elif players_pick == 'Rock' and computers_pick == 'Paper':
    print('You lose!')
    losses += 1
  elif players_pick == "Paper" and computers_pick == "Scissors":
    print('You lose!')
    losses += 1
  elif players_pick == "Scissors" and computers_pick == "Rock":
    print('You lose!')
    losses += 1       
