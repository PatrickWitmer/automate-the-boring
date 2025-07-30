blackEagle = ['guitar', 'enchanter', 'spacecadet', 'cocaptain']

jabba = ['livin']

sang = []

shmo = ['rainbows', 'necromancers']

def commaList(myList):
  # Test if the list is empty and if so, just return an empty string
  if not myList:
    print('.')
    return
  # If there is just one item in the list, just print that one item in index 0
  if len(myList) == 1:
    print(myList[0])
    return
  # If there is just twoo items in the list, just print those 2 with and in between
  if len(myList) == 2:
    print(' and '.join(myList))
    return
  # Join all but the last item, then add ", and <last item>"
  result = ', '.join(myList[:-1]) + ', and ' + myList[-1]

  print(result)

commaList(blackEagle)
commaList(jabba)
commaList(sang)
commaList(shmo)