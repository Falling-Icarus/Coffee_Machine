from menu import MENU
from menu import resources

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

def check_product(boards, order):
    missing_list = []
    x = order['water'] < boards['water']
    if x == True:
        missing_list.append('water')
    y = order['milk'] == True and order['milk'] < boards['milk']
    if y == True:
        missing_list.append('milk')
    z =  order['coffee'] < boards['coffee']
    if z == True:
        missing_list.append('coffee')
    if len(missing_list) != 0:
        for i in missing_list:
            return print(f"Sorry, there is not enough {i}!")

def price():
    print("Please insert coins.")
    coins = []
    quarters = int(input("How many quarters?: "))
    coins.append(quarter * quarters)
    dimes = int(input("How many dimes?: "))
    coins.append(dime * dimes)
    nickles = int(input("How many nickles?: "))
    coins.append(nickel * nickles)
    pennies = int(input("how many pennies?: "))
    coins.append(penny * pennies)
    total = sum(coins)
    values = MENU['espresso']['cost'] or MENU['latte']['cost'] or MENU['cappuccino']['cost']
    if total > values:
        change = total - values
        return print(f"Here is {round(change, 2)} in change.")
    else:
        return print("Sorry that's not enough money. Money refunded.")


def coffee_machine():
    commander = False
    total_value = 0
    while commander == False:

        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "report":
            for i, t in resources.items():
                print(f"{i, t}ml")
            print(f"Money: {total_value}")

        elif choice == "espresso":
            if check_product(MENU['espresso']['ingredients'], resources) == True:
                coffee_machine()
            else:
                price()
                resources['water'] -= 50
                resources['coffee'] -= 18
                total_value += MENU['espresso']['cost']
                print("Here is your espresso☕️. Enjoy!")

        elif choice == "latte":
            if check_product(MENU['latte']['ingredients'], resources) == True:
                coffee_machine()
            else:
                price()
                resources['water'] -= 200
                resources['milk'] -= 150
                resources['coffee'] -= 24
                total_value += MENU['latte']['cost']
                print("Here is your latte☕. Enjoy!")

        elif choice == "cappuccino":
            if check_product(MENU['cappuccino']['ingredients'], resources) == True:
                coffee_machine()
            else:
                price()
                resources['water'] -= 250
                resources['milk'] -= 100
                resources['coffee'] -= 24
                total_value += MENU['cappuccino']['cost']
                print("Here is your cappuccino☕. Enjoy!")

        elif choice == "off":
            commander = True

        else:
            if check_product(MENU['espresso']['ingredients'], resources) == True:
                commander = False

coffee_machine()