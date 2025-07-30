import random

number_of_streaks = 0
experiments = 10000  # Number of experiments

for experiment_number in range(experiments):
    # Generate 100 random coin flips: 'H' for heads, 'T' for tails
    flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')

    # Check for a streak of 6 heads or 6 tails
    for i in range(len(flips) - 5):  # Stop at index 94 (last possible streak start)
        if flips[i:i + 6] == ['H'] * 6 or flips[i:i + 6] == ['T'] * 6:
            number_of_streaks += 1
            break  # Found a streak, no need to keep checking

# Calculate and display percentage
print('Chance of streak: %s%%' % (number_of_streaks / 100))
