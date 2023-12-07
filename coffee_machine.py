# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:17:00 2023

@author: Ananya
"""
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def check_resources(choice, resources, menu):
    is_check = True    
    for item in menu['ingredients']:
        if (resources[item]-menu['ingredients'][item]) < 0:
            print("“Sorry there is not enough {item}.")
            is_check = False    
    else:
        is_check = True
    return is_check


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.10
    total += int(input("how many nickel?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total


def Check_transaction(coin,menu):
    if coin < menu['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += menu['cost']
        coin = round(coin-menu['cost'],2)
        if coin > 0:
            print(f"Here is ${coin} dollars in change")
        return True
    
def prepare_coffee(user_choice,menu):
    for item in menu:
        resources[item]-=menu[item]
        
    
def coffee_machine():
    from data import MENU
    
    is_running = True
    while is_running:
        # Prompt user by asking their coffee choice
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # Turn off the Coffee Machine for Maintenance activity
        if user_choice == "off":
            is_running = False
        elif user_choice == "report":
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffee: {resources['coffee']}")
            print(f"Profit: ${round(profit,2)}")
        elif user_choice in ("espresso", "latte", "cappuccino"):
            is_check = check_resources(user_choice, resources, MENU[user_choice])
            if is_check:
                coin=process_coins()
                if Check_transaction(coin, MENU[user_choice]):
                    prepare_coffee(user_choice,MENU[user_choice]['ingredients'])                    
                    print(f"Here is your {user_choice}☕. Enjoy!")
        else:
            print("Wrong Input!")
            

coffee_machine()
