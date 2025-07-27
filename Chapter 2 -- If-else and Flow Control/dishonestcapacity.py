print('Enter TB or GB for the Advertised Unit:')
unit = input('>')

# Calculate the amount that the advertising lies:
if unit == 'TB' or 'tb':
  discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
  discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest 100th,
# and convert it to a string so it can be concatenated.
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + unit)
