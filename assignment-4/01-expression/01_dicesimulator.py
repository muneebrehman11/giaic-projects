import random

def main():
    # Simulate rolling two dice three times
    for i in range(1, 4):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("Roll", i, ": Die 1 =", die1, "Die 2 =", die2)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
