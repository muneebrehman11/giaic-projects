def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    # Example usage:
    print(in_range(5, 1, 10))   # True
    print(in_range(0, 1, 10))   # False
    print(in_range(10, 1, 10))  # True
    print(in_range(11, 1, 10))  # False

if __name__ == '__main__':
    main()
