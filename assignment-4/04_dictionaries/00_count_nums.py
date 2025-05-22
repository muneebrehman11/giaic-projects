def main():
    counts = {}
    while True:
        num_str = input("Enter a number: ")
        if num_str.strip() == "":
            break
        num = num_str.strip()
        # Count occurrences (as strings since input is string)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for number, count in counts.items():
        print(f"{number} appears {count} times.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
