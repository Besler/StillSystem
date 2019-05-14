
# Imports
import os
from Controller import Controller

# Defaults
CUFF_PIN 		= 17				# 0 in wPi
BLADDER_PIN = 27				# 2 in wPi
filename  = './data/The Old Man and the Sea - Narrated by Charlton Heston full audio book.mp3'

c = Controller(CUFF_PIN, BLADDER_PIN, filename)
os.sys.exit(c.run())

