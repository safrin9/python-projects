MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(resources, money):
    print("water: " + str(resources["water"]))
    print("milk: " + str(resources["milk"]))
    print("coffee: " + str(resources["coffee"]))
    print("money: $" + str(money))


def is_sufficient(ingredients):
     for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f" sorry! not enough {item}")
            return False
     return True


def coin():

    print("Please insert coins. ")
    quarter = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    penny = int(input("how many pennies?: "))
    money = quarter * 0.25 + dimes * 0.1 + nickles * 0.05 + penny * 0.01
    return money

def check(money, cost):
    if money >= cost:
      change = round(money - cost, 2)
      print(f"Here is ${change} in change.")
      global profit
      profit += cost
      return True
    else:
      print("Sorry that's not enough money. Money refunded.")
      return False




def make_coffee(coffee, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    return f"Here's your {coffee}. Enjoy! "


is_on = True
while is_on:
    cof = input("What would you like? (espresso/latte/cappuccino):")
    if cof == "off":
        is_on = False
    elif cof == "report":
        report(resources, profit)
    else:
        drink = MENU[cof]
        if is_sufficient(drink["ingredients"]):
            payment = coin()
            if check(payment, drink["cost"]):
                print(make_coffee(cof, drink["ingredients"]))


