def main():
    # Prompt the user for length in feet
    feet = float(input("Enter length in feet: "))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12

    # Display the result
    print(str(feet) + " feet is " + str(inches) + " inches")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
