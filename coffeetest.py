from coffeecontrol import BrewCoffee

if __name__=="__main__":
    print("testing coffee machine")
    coffee_choice="darkroast"
    brew=BrewCoffee(coffee_choice)
    brew.pourBean()