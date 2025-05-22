ADULT_AGE = 18

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == '__main__':
    main()
