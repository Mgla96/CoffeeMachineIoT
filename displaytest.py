from coffeecontrol import BrewCoffee
from twitter import Twitter
import time

if __name__=="__main__":
    twit=Twitter()
    coffee_choice,amount_votes=twit.getVote()
    print(coffee_choice,amount_votes)
    brew=BrewCoffee(coffee_choice)
    brew.displayCoffeeChoice(coffee_choice,amount_votes)
    #brew.pourBean()