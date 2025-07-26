print('Hello World')

print('What is your name?') # Ask for their name.
my_name = input('>')

print('Good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))

print('What is your age?') # Ask for their Age.
my_age = input('>')
int_age = int(my_age)

if int_age >= 40:
  print('You are over the hill guy.')
else:
  print('You still have some time.')  

print('The length of your age is:')
print(len(my_age))

print('Your age will be ' + str(int(my_age) + 1) + ' in a year.')