def main():
    # Constant speed of light in m/s
    C = 299792458

    # Prompt the user for mass in kilograms
    mass = float(input("Enter kilos of mass: "))

    # Display formula steps
    print("\ne = m * C^2...\n")
    print("m =", mass, "kg")
    print("C =", C, "m/s")

    # Calculate energy using Einstein's formula
    energy = mass * C**2

    # Display the result
    print("\n" + str(energy) + " joules of energy!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
