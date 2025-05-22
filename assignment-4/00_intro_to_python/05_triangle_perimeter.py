def main():
    # Prompt user for each side length
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print the result
    print("The perimeter of the triangle is", perimeter)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
