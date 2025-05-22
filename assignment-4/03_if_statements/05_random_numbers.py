import random

def main():
    for _ in range(10):
        print(random.randint(1, 100), end=" ")
    print()  # for newline after printing all numbers

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
