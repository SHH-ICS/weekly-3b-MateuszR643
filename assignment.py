print("Dezmond's Pizzeria menu:")
print("1. Large Pizza: $6.00")
print("2. Extra Large Pizza: $10.00")
size = input("Please input the number of the menu item you are ordering. ")
toppings = input("How many toppings do you want? \n 1 - $1.00 \n 2 - $1.75 \n 3 - $2.50 \n 4 - $3.35")
pizzaprices = [6.00, 10.00]
topprices = [1.00, 1.75, 2.50, 3.35]
price = 0.00

if txt.isnumeric(size) and isinstance(size) == int:
    size = int(size)
    if size <= 2 and size > 0:
        if txt.isnumeric(toppings) and isinstance(toppings) == int:
            toppings = int(toppings)
            if toppings <= 4 and toppings >= 0:
                calculateprice()
    else:
        print("Input not in range of menu.")
else:
    print("Please input a numerical value from the menu")

def calculateprice():
    if not toppings == 0:
        price += pizzaprices[size-1] + topprices[toppings-1]
    print("You ordered:", size, "and", toppings, "toppings")