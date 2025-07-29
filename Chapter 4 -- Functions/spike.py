import time, sys

def spikey(low, high):
  try:
    while True: # Main program loop
    # Draw lines with increasing length
      for i in range(low, high):
        print('-' * (i * i))
        time.sleep(0.1)

      for i in range(high, low, -1):
        print('-' * (i * i))
        time.sleep(0.1)
  except KeyboardInterrupt:
    sys.exit()

spikey(1, 30)    