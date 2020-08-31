#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


#gpio-5 is 20kg servo
#gpio-18 is 25kg servo
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

class BrewCoffee():
    def __init__(self, coffeechoice):
        self.coffeechoice=coffeechoice
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BCM)
        #SETTING UP RELAYS
        gpioList = [26, 19, 13, 6, 12, 16, 20, 21]
        #21 will be the mixer
        for i in gpioList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        #SETTING UP SERVOS
        #gpio-5 is 20kg servo
        #gpio-18 is 25kg servo
        # Set pin 5 as an output, and set servo1 as pin 5 as PWM
        GPIO.setup(5,GPIO.OUT)
        self.servo1 = GPIO.PWM(5,50) # Note 5 is pin, 50 = 50Hz pulse
        # Set pin 18 as an output, and set servo1 as pin 5 as PWM
        GPIO.setup(18,GPIO.OUT)
        self.servo2 = GPIO.PWM(18,50) # Note 5 is pin, 50 = 50Hz pulse

    def startHotWater(self):
        print("starting hot water")

    def pourWater(self):
        print("pouring water")
        self.servo2.start()
        pour(self.servo2,4)
        self.servo2.stop()

    def pourBean(self):
        print(self.coffeechoice,"was chosen. Pouring the beans")
    
    def mix(self):
        #21 is mixer
        try:
            GPIO.output(21, GPIO.LOW)
            time.sleep(15)
            GPIO.output(21, GPIO.HIGH)
        except:
            print("Quit")
            # Reset GPIO settings
            GPIO.cleanup()

    def steep(self):
        print("steeping for 4 minutes")
        time.sleep(240)


    

    


    
            

