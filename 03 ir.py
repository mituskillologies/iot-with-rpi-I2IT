import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
try:
	while True:
		i = GPIO.input(18)
		if i==1:
			print("No Obstacle")
			time.sleep(0.1)
		elif i==0:
			print("Obstacle Found")
			time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()


	
