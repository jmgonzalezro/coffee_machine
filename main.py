MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

PROFIT = 0
RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_report():
    water_level = RESOURCES["water"]
    milk_level = RESOURCES["milk"]
    coffee_level = RESOURCES["coffee"]

    print(f"Water: {water_level}\n"
          f"Milk: {milk_level}\n"
          f"Coffe:{coffee_level}\n"
          f"Money: {profit}")


def ask_for_coffe():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "espresso":
        print(f"You have chossen {coffee_type}.")
        return 'espresso'
    elif coffee_type == "latte":
        print(f"You have chossen {coffee_type}.")
        return 'latte'
    elif coffee_type == "cappuccino":
        print(f"You have chossen {coffee_type}.")
        return 'capuccino'
    elif coffee_type == "off":
        print("Shutting down the Coffe Machine.")
        return exit()
    elif coffee_type == "report":
        return get_report()
    else:
        print("Please, select or type a propper coffe type.")
        ask_for_coffe()

def get_coffee_ingredients(coffee_choosen):
    return MENU[coffee_choosen]["ingredients"]


def check_resources(coffee_type: str):
    coffee_ingredients = get_coffee_ingredients(coffee_type)
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > RESOURCES[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")


def money_inserted(nquarters, ndimes, nnickles, npennie):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    total = nquarters * quarters + ndimes * dimes + nnickles * nickles + npennies * pennies

    return round(total, 2)


def check_transaction_success(money_inserted, coffe_cost):
    money_inserted = money_inserted
    coffe_cost = coffe_cost

    if money_inserted < coffe_cost:
        print("Sorry, that's not enough money. Money refunded.")
    elif money_inserted > coffe_cost:
        print('Refunding money')
    else:
        return money_inserted
    
    PROFIT = profit
        
def make_coffe():
    ask_for_coffe()
