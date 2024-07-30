import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
#Connect buzzer to GPIO18 
while True:
    print("BUZZER on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print("BUZZER off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)


