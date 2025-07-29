import random

# flip a coin
flip_coin = random.randint(1, 2)

# we need to assign heads or tails string to the int 1 or 2

if flip_coin == 1:
  coin_face = "Heads"
else:
  coin_face = "Tails"  

# Let Blackeagle know what is on the coin
print('Hey Blackeagle, the coin flipped a ' + coin_face)

# if the coin is heads, we get tail, if the coin is tails, we get head
if coin_face == "Heads":
  print('Hey blackeagle you are getting tail tonight!')
else:
  print('Hey blackeagle you are getting head tonight!')
