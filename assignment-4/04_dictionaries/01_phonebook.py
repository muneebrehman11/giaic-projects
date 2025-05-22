def main():
    phonebook = {}

    # Add some entries
    phonebook["Alice"] = "123-456-7890"
    phonebook["Bob"] = "555-123-4567"
    phonebook["Charlie"] = "987-654-3210"

    # Lookup a name
    name = input("Enter a name to look up their phone number: ")
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"No entry found for {name}")

    # Print the entire phonebook
    print("\nPhonebook entries:")
    for person, number in phonebook.items():
        print(f"{person}: {number}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
