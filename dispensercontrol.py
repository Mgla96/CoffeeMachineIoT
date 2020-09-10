#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
#gpio-18 is 25kg servo

#gpio-4,gpio-5,gpio-17, are coffee bean dispensers
#def setServoPulse(pin,ms_on):
#	pin.write_analog(1023*ms_on/20)
	
def setAngle(angle,pwm):
	duty = angle / 18 + 2
	GPIO.output(5, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(5, False)
	pwm.ChangeDutyCycle(0)

def pour(pwm):
	GPIO.output(5,True)
	for i in range(10):
		setAngle(0,pwm)
		setAngle(180,pwm)
	setAngle(0,pwm)


def pressButton(pwm):
    setAngle(0,pwm)
    print("press button")
    setAngle(180,pwm)
    time.sleep(1)
    setAngle(0,pwm)

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
servo1 = GPIO.PWM(4,50) # Note 4 is pin, 50 = 50Hz pulse
GPIO.setup(5,GPIO.OUT)
servo2 = GPIO.PWM(5,50) # Note 5 is pin, 50 = 50Hz pulse
GPIO.setup(17,GPIO.OUT)
servo3 = GPIO.PWM(17,50) # Note 17 is pin, 50 = 50Hz pulse
servo1.start(0)
servo2.start(0)
servo3.start(0)

time.sleep(1)
print("testing dark roast")
pour(servo1)
servo1.stop()
print("testing medium roast")
pour(servo2)
servo2.stop()
print("testing light roast")
pour(servo3)
servo3.stop()
GPIO.cleanup()
print ("Complete")