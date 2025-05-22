def main():
    numbers = [1, 2, 3, 4]  # Original list
    for i in range(len(numbers)):
        numbers[i] *= 2  # Double each element
    print("Doubled list:", numbers)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()