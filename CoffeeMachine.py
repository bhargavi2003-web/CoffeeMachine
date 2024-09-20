from random import choice
from traceback import print_exc

MENU = {
    "espresso": {
        "ingredients": {
            "wtaer": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "wtaer": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "wtaer": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.5,
    }

}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
def is_resource_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough resource{item}")
            return False
    return True

def process_coins():
    """ Return the total coins inserted"""
    print("please insert coins.")
    total = int(input("how many quarters do you have?"))*0.25
    total += int(input("how many dimes do you have?"))*0.1
    total += int(input("how many nicks do you have?"))*0.05
    total += int(input("how many pennies do you have?"))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in changes.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry there is not enough money{money_received}")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} Enjoyy")


is_on = True
while True:
    choice = input("What do you want to do? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_available(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
