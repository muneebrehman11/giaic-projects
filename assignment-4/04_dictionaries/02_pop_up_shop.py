def main():
    # Dictionary of fruits with their prices
    fruit_prices = {
        "apple": 5,
        "durian": 20,
        "jackfruit": 10,
        "kiwi": 7.5,
        "rambutan": 15,
        "mango": 12
    }

    total_cost = 0.0

    # Loop through each fruit and ask user for quantity
    for fruit, price in fruit_prices.items():
        qty = input(f"How many ({fruit}) do you want?: ")
        # Convert to int safely (assuming valid integer input)
        qty = int(qty)
        total_cost += qty * price

    print(f"Your total is ${total_cost}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
