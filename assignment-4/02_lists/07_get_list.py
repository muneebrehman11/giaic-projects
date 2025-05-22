def main():
    values = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        values.append(value)
    print("Here's the list:", values)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
