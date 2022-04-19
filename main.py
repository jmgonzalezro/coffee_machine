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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_report():
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]

    print(f"{water_level}")
    print(f"{milk_level}")
    print(f"{coffee_level}")
    print(f"Money: {profit}")


def ask_for_coffe():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "espresso":
        print(f"You have chossen {coffee_type}")
    elif coffee_type == "latte":
        print(f"You have chossen {coffee_type}")
    elif coffee_type == "cappuccino":
        print(f"You have chossen {coffee_type}")
    elif coffee_type == "off":
        print("Shutting down the Coffe Machine")
    elif coffee_type == "report":
        get_report()
    else:
        print("Please, select or type a propper coffe type")

    ask_for_coffe()


def get_coffee_ingredients(coffee_choosen):
    return MENU[coffee_choosen]["ingredients"]


def check_resources(coffee_type: str):
    coffee_ingredients = get_coffee_ingredients(coffee_type)
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")


def coin_processor():
    pass
