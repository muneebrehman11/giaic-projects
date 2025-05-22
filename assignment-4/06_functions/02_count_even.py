def count_even(lst):
    # Count how many numbers in lst are even
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def main():
    numbers = []
    while True:
        inp = input("Enter an integer or press enter to stop: ")
        if inp == '':
            break
        try:
            num = int(inp)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid integer or press enter to stop.")
    count_even(numbers)

if __name__ == '__main__':
    main()
