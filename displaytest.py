#from coffeecontrol import BrewCoffee
from twitter import Twitter
import time

if __name__=="__main__":
    twit=Twitter()
    coffee_choice,amount_votes=twit.getVote()
    #coffee_choice,amount_votes="darkroast",1
    print(coffee_choice,amount_votes)
    '''
    brew=BrewCoffee(coffee_choice)
    print(coffee_choice,amount_votes)
    brew.displayCoffeeChoice(coffee_choice,amount_votes)
    brew.pourBean()
    brew.closeTop()
    brew.startBrew()
    brew.clearCoffeeChoice()
    '''