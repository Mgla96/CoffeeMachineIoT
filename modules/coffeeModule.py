 
#You can import any required modules here
from coffeecontrol import BrewCoffee
from twitter import Twitter
import time

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

moduleName = "coffeeModule"
#All of the words must be heard in order for this module to be executed
commandWords = ["make","coffee"]

def execute(command):
    print("Gathering Twitter Vote")
    twit=Twitter()
    coffee_choice=twit.getVote()
    
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial, rotate=0)
    notify = coffee_choice+" was chosen!"
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((10, 40), notify, fill="white")

    brew=BrewCoffee(coffee_choice)
    brew.startHotWater()
    brew.pourBean()
    #brew.waitToBoil
    brew.pourWater()
    brew.mix()
    #brew.steep()
    return