#You can import any required modules here
from coffeecontrol import BrewCoffee
from twitter import Twitter
import time

# Import all board pins.
from board import SCL, SDA
import busio
# Import the SSD1306 module.
import adafruit_ssd1306
import digitalio
from PIL import Image, ImageDraw, ImageFont


def displayCoffeeChoice(coffee_choice):
    i2c = busio.I2C(SCL, SDA)
    display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    display.fill(0)
    display.show()
    # Create blank image for drawing.
    image = Image.new("1", (display.width, display.height))
    draw = ImageDraw.Draw(image)
    # Load a font in 2 different sizes.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    # Draw the text
    draw.text((0, 0), coffee_choice, font=font, fill=255)
    draw.text((0, 15), "selected!", font=font2, fill=255)
    
    # Display image
    display.image(image)
    display.show()
    #time.sleep(30)
    #display.fill(0)
    #display.show()

        # Open, resize, and convert image to Black and White
    image = (
        Image.open('static/images/Poe.jpg')
        .resize((display.width, display.height), Image.BICUBIC)
        .convert("1")
    )
    # Display the converted image
    display.image(image)
    display.show()

if __name__=="__main__":
    #twit=Twitter()
    #coffee_choice=twit.getVote()
    coffee_choice="medium roast"
    displayCoffeeChoice(coffee_choice)