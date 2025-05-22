MAX_VALUE = 10000

def main():
    a, b = 0, 1
    # Print Fibonacci numbers while a is less than MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=' ')
        a, b = b, a + b
    print()  # for newline after finishing

if __name__ == '__main__':
    main()
