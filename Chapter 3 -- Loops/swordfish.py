while True:
  print('Who are you?')
  name = input('>')
  if name != "Joe":
      continue
  print('What is your password? (Hint: it is a fish.)')
  password = input('>')
  if password == 'swordfish':
    break
print('Login Succesful!')