#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
# Import all board pins.
from board import SCL, SDA
import busio
# Import the SSD1306 module.
import adafruit_ssd1306
import digitalio
from PIL import Image, ImageDraw, ImageFont

class BrewCoffee():
    def __init__(self, coffeechoice):
        self.coffeechoice=coffeechoice.lower()
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BCM)
        #SETTING UP RELAYS
        gpioList = [26, 19, 13, 6, 12, 16, 20, 21]
        #21 will be the mixer
        for i in gpioList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        #SETTING UP SERVOS (gpio-5: 20kg servo) (gpio-18 is 25kg servo)
        # Set pin 5 as an output, and set servo1 as pin 5 as PWM
        GPIO.setup(5,GPIO.OUT)
        self.servo1 = GPIO.PWM(5,50) # Note 5 is pin, 50 = 50Hz pulse
        self.servo1.start(0)
        # Set pin 18 as an output, and set servo1 as pin 5 as PWM
        GPIO.setup(18,GPIO.OUT)
        self.servo2 = GPIO.PWM(18,50) # Note 5 is pin, 50 = 50Hz pulse
        self.servo2.start(0)

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
            pour(self.servo2,6)
            self.servo2.stop()
        except:
            print("Quit pour water")
            # Reset GPIO settings
            GPIO.cleanup()

    def pourBean(self):
        print(self.coffeechoice,"was chosen. Pouring the beans")
        if self.coffeechoice=="lightroast":
            print("light roast")
        elif self.coffeechoice=="mediumroast":
            print("medium roast")
        elif self.coffeechoice=="darkroast":
            print("dark roast")
        else:
            print(self.coffeechoice,"is not one of the 3 choices so defaulting to dark")
            self.coffeechoice="darkroast"
    
    def mix(self):
        print("Mix Coffee")
        #21 is mixer
        try:
            GPIO.output(21, GPIO.LOW)
            time.sleep(15)
            GPIO.output(21, GPIO.HIGH)
        except:
            print("Quit mix")
            # Reset GPIO settings
            GPIO.cleanup()

    def waitToBoil(self):
        print("Waiting 8 minutes for water to boil")
        time.sleep(480)

    def steep(self):
        print("steeping for 4 minutes")
        time.sleep(240)

    def displayCoffeeChoice(self, coffee_choice,amount_votes):
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
        i2c = busio.I2C(SCL, SDA)
        display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        display.fill(0)
        display.show()
    
    def displayFace(self):
        i2c = busio.I2C(SCL, SDA)
        display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        display.fill(0)
        display.show()
        image = (Image.open('static/images/Poe.jpg').resize((display.width, display.height), Image.BICUBIC).convert("1"))
        display.image(image)
        display.show()



        

        


    
            

