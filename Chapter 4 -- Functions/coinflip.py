import random
for i in range(100):  # Perform 100 coin flips.
    if random.randint(0, 1) == 0:
        print('H')
    else:
        print('T')
print()  # Print one newline at the end.