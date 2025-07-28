import random
# for i in range(5):
#   print(random.randint(1, 10))

# Let's make an everquest version!

print('We are rolling on loot')
print('Enter a number to random the range (e.g. 666)')
number = input('>')

print(f'^^A Magic Die is rolled by @sanguine_______. **It could have been any number from 0 to {number} but this time it turned up a {(random.randint(0, int(number)))}')