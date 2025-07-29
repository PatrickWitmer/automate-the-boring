# Start a list named cats to store our cat's names
cats = []

# Run a loop that keeps asking for cat names until we don't have any left, add them to the cats list, then exit the loop
while True:
  print('Enter the name of cat ' + str(len(cats) + 1) + ' (Or enter nothing to stop.):')
  name = input()
  if name == '':
    break
  cats = cats + [name]

print('The cat names are:')
for name in cats:
  print('   ' + name)
