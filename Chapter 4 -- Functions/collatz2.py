# Function named collatz() that checks if a number is even or odd, prints the number, then returns a new number (result) motified by number // 2 (even) or 3 * number + 1 (odd)

def collatz(number):
  if number % 2 == 0:
    result = number // 2
    print(result, end=' ')
    return result
  else:
    result = 3 * number + 1
    print(result, end=' ')
    return result  

# Ask the user to enter a number that we can use in collat()
while True:
  try:
    print('Please enter a number:')
    user_number = int(input('>'))
    break
  except ValueError:
    print('That is not a valid number.')

print(user_number, end=' ')    
# Call the funtionclear until the number returned is one
while user_number != 1:
  user_number = collatz(user_number)

