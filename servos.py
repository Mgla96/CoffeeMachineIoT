#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
#gpio-5 is 20kg servo
def setAngle(angle,pwm):
	duty = angle / 18 + 2
	GPIO.output(5, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(5, False)
	pwm.ChangeDutyCycle(0)

def pour(pwm,tm):
	setAngle(0,pwm)
	print("pouring hot water")
	setAngle(90,pwm)
	time.sleep(tm)
	setAngle(0,pwm)

def pressButton(pwm):
    setAngle(0,pwm)
    print("press button")
    setAngle(180,pwm)
    time.sleep(1)
    setAngle(0,pwm)

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)
# Set pin 5 as an output, and set servo1 as pin 5 as PWM
GPIO.setup(5,GPIO.OUT)
servo1 = GPIO.PWM(5,50) # Note 5 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 1 seconds")
time.sleep(1)

#pouring
pour(servo1,4)

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")
