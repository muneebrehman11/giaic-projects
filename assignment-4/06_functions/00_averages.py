def average(num1, num2):
    return (num1 + num2) / 2

def main():
    # Example usage:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    avg = average(a, b)
    print(f"The average of {a} and {b} is {avg}")

if __name__ == '__main__':
    main()
