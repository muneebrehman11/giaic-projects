def num_in_stock(fruit):
    # Inventory dictionary for Sophia's fruit store
    inventory = {
        "apple": 500,
        "banana": 300,
        "orange": 0,
        "pear": 1000,
        "grape": 200
    }
    # Return the quantity, 0 if fruit not found
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
