def main():
    min_height = 50
    height_str = input("How tall are you? ")
    if height_str.strip() == "":
        print("No height entered.")
        return

    height = float(height_str)
    if height >= min_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

