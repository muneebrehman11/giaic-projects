def add_three_copies(lst, data):
    for _ in range(3):
        lst.append(data)  # Modify the list directly

def main():
    message = input("Enter a message to copy: ")
    messages_list = []

    print("\nList before:", messages_list)
    add_three_copies(messages_list, message)
    print("List after:", messages_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
