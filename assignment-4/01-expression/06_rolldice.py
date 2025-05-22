import random

def main():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Roll 1: {die1}")
    print(f"Roll 2: {die2}")
    print(f"Total: {die1 + die2}")

if __name__ == '__main__':
    main()
