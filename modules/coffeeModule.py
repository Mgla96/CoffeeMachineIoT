 
#You can import any required modules here
from coffeecontrol import BrewCoffee
from twitter import Twitter
import time
#This can be anything you want
moduleName = "coffeeModule"

#All of the words must be heard in order for this module to be executed
commandWords = ["make","coffee"]

def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' parameter is the command you speak
    print("Gathering Twitter Vote")
    twit=Twitter()
    coffee_choice=twit.getVote()
    brew=BrewCoffee(coffee_choice)
    #brew.startHotWater()
    brew.pourBean()
    #time.sleep(480) #8 minutes waiting for water to boil
    #brew.pourWater()
    #brew.mix()
    #brew.steep()
    return