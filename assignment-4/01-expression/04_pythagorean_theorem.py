import math

def main():
    # Prompt the user for the lengths of AB and AC
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse BC
    bc = math.sqrt(ab**2 + ac**2)

    # Display the result
    print("The length of BC (the hypotenuse) is:", bc)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
