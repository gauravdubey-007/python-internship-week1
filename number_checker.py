"""Even/Odd and Prime Number Checker."""


def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=== Even/Odd & Prime Number Checker ===")
    while True:
        n = get_integer("\nEnter a number: ")

        print(f"{n} is an {'even' if is_even(n) else 'odd'} number.")
        print(f"{n} is {'a prime' if is_prime(n) else 'not a prime'} number.")

        again = input("\nCheck another number? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
