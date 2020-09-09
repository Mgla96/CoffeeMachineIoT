#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

import busio
from board import SCL, SDA
import busio
# Import the SSD1306 module.
import adafruit_ssd1306
import digitalio
from PIL import Image, ImageDraw, ImageFont

class BrewCoffee():
    def __init__(self, coffeechoice):
        self.coffeechoice=coffeechoice.lower()
        GPIO.setmode(GPIO.BCM)
        #SETTING UP RELAYS
        gpioList = [26, 19, 13, 6, 12, 16, 20, 21]
        for i in gpioList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        #SETTING UP SERVOS
        #Dark Roast
        GPIO.setup(4,GPIO.OUT)
        self.servo1 = GPIO.PWM(4,50) # Note 4 is pin, 50 = 50Hz pulse    
        self.servo1.start(0)
        #Medium Roast
        GPIO.setup(5,GPIO.OUT)
        self.servo2 = GPIO.PWM(5,50) # Note 5 is pin, 50 = 50Hz pulse
        self.servo2.start(0)
        #Light Roast
        GPIO.setup(17,GPIO.OUT)
        self.servo3 = GPIO.PWM(17,50) # Note 17 is pin, 50 = 50Hz pulse
        self.servo3.start(0)
        #Hot Water Pourer (25kg servo)
        GPIO.setup(18,GPIO.OUT)
        self.water_pourer_servo = GPIO.PWM(18,50) # Note 17 is pin, 50 = 50Hz pulse
        self.water_pourer_servo.start(0)

    def startHotWater(self):
        print("starting hot water")
        
    def pourWater(self):
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
        try:
            print("pouring water started")
            pour(self.water_pourer_servo,6)
            self.water_pourer_servo.stop()
        except:
            print("Quit pour water")
            GPIO.cleanup()

    def pourBean(self):
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

        print(self.coffeechoice,"was chosen. Pouring the beans")
        if self.coffeechoice=="darkroast":
            pour(self.servo1)
        elif self.coffeechoice=="mediumroast":
            print("medium roast")
            pour(self.servo2)
        elif self.coffeechoice=="lightroast":
            print("dark roast")
            pour(self.servo3)
        else:
            print(self.coffeechoice,"is not one of the 3 choices so defaulting to medium")
            self.coffeechoice="mediumroast"
            pour(self.servo2)
    
    def mix(self):
        '''
        GPIO-21 is Mixer
        '''
        print("Mix Coffee")
        try:
            GPIO.output(21, GPIO.LOW)
            time.sleep(15)
            GPIO.output(21, GPIO.HIGH)
        except:
            print("Quit mix")
            # Reset GPIO settings
            GPIO.cleanup()

    def waitToBoil(self):
        '''
        Sets timer to wait for water to boil
        '''
        print("Waiting 8 minutes for water to boil")
        time.sleep(480)

    def steep(self):
        '''
        After coffee mixed in french press, sets timer for steeping the beans before the coffee is ready
        '''
        print("steeping for 4 minutes")
        time.sleep(240)

    def displayCoffeeChoice(self, coffee_choice,amount_votes):
        '''
        Shows on OLED Screen the coffee choice that was chosen through Twitter
        '''
        print(amount_votes)
        i2c = busio.I2C(SCL, SDA)
        display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        display.fill(0)
        display.show()
        image = Image.new("1", (display.width, display.height))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
        font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        draw.text((0, -3), "Twitter Voted For", font=font, fill=255)
        draw.text((0, 8), coffee_choice, font=font2, fill=255)
        draw.text((0, 20), "# votes: "+str(amount_votes), font=font, fill=255)
        display.image(image)
        display.show()
        
    def clearCoffeeChoice(self):
        '''
        Clears the Coffee Choice on the OLED Screen
        '''
        i2c = busio.I2C(SCL, SDA)
        display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        display.fill(0)
        display.show()
    
    def displayFace(self):
        '''
        Displays a face on the OLED Screen for fun
        '''
        i2c = busio.I2C(SCL, SDA)
        display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        display.fill(0)
        display.show()
        image = (Image.open('static/images/Poe.jpg').resize((display.width, display.height), Image.BICUBIC).convert("1"))
        display.image(image)
        display.show()



        

        


    
            

