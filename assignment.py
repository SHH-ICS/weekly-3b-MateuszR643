print("Dezmond's Pizzeria menu:")
print("1. Large Pizza: $6.00")
print("2. Extra Large Pizza: $10.00")
size = input("Please input the number of the menu item you are ordering. ")
toppings = input("How many toppings do you want? \n 0 - $0.00\n 1 - $1.00 \n 2 - $1.75 \n 3 - $2.50 \n 4 - $3.35 \n")
pizzaprices = [6.00, 10.00]
topprices = [0.00, 1.00, 1.75, 2.50, 3.35]

def calculateprice():
    tax = pizzaprices[size-1]*0.13 + topprices[toppings]*0.13
    price = round(pizzaprices[size-1] + topprices[toppings] + tax, 2)
    print("You ordered: item", size, "and", toppings, "toppings \n Your total is: $" + str(price), "\n Thank you for ordering from Dezmond's Pizzeria!")

if size == "1" or size == "2":
    size = int(size)
    if toppings == "0" or toppings == "1" or toppings == "2" or toppings == "3" or toppings == "4":
        toppings = int(toppings)
        calculateprice()
    else:
        print("Input not in range of topppings.")
else:
    print("Please input a numerical value from the menu.")