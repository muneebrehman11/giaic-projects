def get_first_element(lst):
    print("First element in the list is:", lst[0])

def main():
    n = int(input("How many elements do you want to add to the list? "))
    lst = []
    for i in range(n):
        element = input(f"Enter element #{i + 1}: ")
        lst.append(element)

    get_first_element(lst)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
