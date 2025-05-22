import random

def main():
    number = random.randint(0, 99)
    guess = None

    print("I am thinking of a number between 0 and 99...")

    while guess != number:
        guess_str = input("Enter a guess: ")
        if not guess_str.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess_str)
        
        if guess > number:
            print("Your guess is too high")
        elif guess < number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {number}")

if __name__ == '__main__':
    main()
