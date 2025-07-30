birthdays = {'WBA': 'Apr 20', 'Shmo': 'Apr 1', 'Princess': 'Apr 2'}

while True:
  print('Enter a name:')
  name = input('')
  if name == '':
    break

  if name in birthdays:
    print(birthdays[name] + ' is the birthday of ' + name)
  else:
    print(f'I do not have a birthday for {name}')
    print('Please enter a birthday for ' + name)
    birthday = input('')
    birthdays[name] = birthday
    print('Birthday updated.')
    print(birthdays)
