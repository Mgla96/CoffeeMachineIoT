 
#You can import any required modules here
from coffeecontrol import brewCoffee
#This can be anything you want
moduleName = "coffeeModule"

#All of the words must be heard in order for this module to be executed
commandWords = ["make","coffee"]

def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' parameter is the command you speak
    print("MAKING COFFEE")
    brewCoffee()
    return