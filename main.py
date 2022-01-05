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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def espresso(list):
    if list["water"] < 50 or list["coffee"] < 18:
        print("Insufficient resources")
    else:
        list["water"] = list["water"] - 50
        list["coffee"] = list["coffee"] - 18
        list["money"] = list["money"] + 1.5
        print("Enjoy your espresso")
    return list


def latte(list):
    if list["water"] < 200 or list["coffee"] < 24 or list["milk"] < 150:
        print("Insufficient resources")
    else:
        list["water"] = list["water"] - 200
        list["coffee"] = list["coffee"] - 24
        list["milk"] = list["milk"] - 150
        list["money"] = list["money"] + 2.5
        print("Enjoy your latte")
    return list


def cappuccino(list):
    if list["water"] < 250 or list["coffee"] < 24 or list["milk"] < 100:
        print("Insufficient resources")
    else:
        list["water"] = list["water"] - 250
        list["coffee"] = list["coffee"] - 24
        list["milk"] = list["milk"] - 100
        list["money"] = list["money"] + 3
        print("Enjoy your cappuccino")
    return list

def payment(price):
    enough = True
    print(f"That will be {price}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    paid = (quarters / 4) + (dimes / 10) + (nickles / 20) + (pennies / 100)
    if paid < price:
        print("Insufficient funds")
        enough = False
        return enough
    elif paid == price:
        return enough
    else:
        left = paid - price
        left = left * 100
        quarters = 0
        dimes = 0
        if left % 25 > 0:
            quarters = (left - (left % 25)) / 25
            left = left - (quarters * 25)
            print(f"Take {quarters} quarters")
            if left % 5 > 0:
                pennies = left % 5
                left = left - pennies
                print(f"Take {pennies} pennies")
            if left % 10 > 0:
                left = left - 5
                print("Take 1 nickle")
            if left > 0:
                dimes = left / 10
                print(f"Take {dimes} dimes")
        else:
            quarters = (left - (left % 25)) / 25
            left = left - (quarters * 25)
            print(f"Take {quarters} quarters")
        return enough

running = True

while running:
    task = input("Do you want to order an espresso, cappuccino, or latte? ").lower()
    if task == "espresso":
        cont = payment(1.5)
        if cont:
            espresso(resources)
    elif task == "cappuccino":
        cont = payment(3)
        if cont:
            cappuccino(resources)
    elif task == "latte":
        cont = payment(2.5)
        if cont:
            lattee("resources")
    elif task == "report":
        print_report()
    elif task == "off":
        print("Goodbye")
        running = False
    else:
        print("Error, wrong input.")