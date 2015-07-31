import time, random
import codebug_i2c_tether

with codebug_i2c_tether.CodeBug() as codebug:
	while True:
		x = random.randint(0,4)
		y = random.randint(0,4)
		onoff = random.randint(0,1)
		codebug.set_pixel(x, y, onoff)
		delay = random.randint(0,10)
		time.sleep (delay / 1000)
		codebug.clear
