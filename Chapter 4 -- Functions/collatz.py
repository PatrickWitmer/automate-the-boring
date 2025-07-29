def collatz(number):
  if number % 2 == 0:
    new_number = number // 2
    print(new_number, end=' ')
    return new_number
  else:
    new_number = 3 * number + 1
    print(new_number, end=' ')
    return new_number

# Ask the user to enter a number

while True:
  try:
    print('Please enter a number:')
    user_number = int(input('>'))
    break
  except ValueError:
    print("Please enter a valid integer.")

print(user_number, end=' ')

while user_number != 1:
   user_number = collatz(user_number)



