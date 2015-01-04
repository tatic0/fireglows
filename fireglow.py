from PyGlow import PyGlow
import time
import random


pyglow = PyGlow()
pyglow.all(0)


colors = ['white','blue','green','yellow','orange','red']
try:
	for b in range(1,500):
		print b
		rbright = random.randrange(10,255,10)
		rcolor = random.choice(colors)
		pyglow.color(rcolor, brightness = rbright)
		time.sleep(0.1)
		pyglow.all(0)  ## if you comment this line, leds stay on util a new color/brightness value ig given)
except KeyboardInterrupt:
	pyglow.all(0)
pyglow.all(0)
