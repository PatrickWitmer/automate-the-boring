import random
# for i in range(5):
#   print(random.randint(1, 10))

# Let's make an everquest version!

print('We are rolling on loot')
print('Enter a number to random the range (e.g. 666)')
str_number = input('>')
int_number = int(str_number)

print('^^A Magic Die is rolled by @sanguine_______. **It could have been any number from 0 to ' + str_number + ' but this time it turned up a ' + str(random.randint(0, int_number)))


