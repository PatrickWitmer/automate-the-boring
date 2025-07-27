# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

print('Please enter a number:')
greeting = input('>')
int_greeting = int(greeting)

if int_greeting == 1:
  print('Hello')
elif int_greeting == 2:
  print('Howdy')
else:
  print('Greetings!')
