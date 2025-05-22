def main():
    # Ask for the dividend
    dividend = int(input("Please enter an integer to be divided: "))

    # Ask for the divisor
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor

    # Print the result
    print("The result of this division is", quotient, "with a remainder of", remainder)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
