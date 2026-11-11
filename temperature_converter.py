"""Temperature Converter: Celsius <-> Fahrenheit using functions."""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Temperature Converter ===")
    while True:
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            c = get_number("Enter temperature in Celsius: ")
            print(f"{c:.2f} °C = {celsius_to_fahrenheit(c):.2f} °F")
        elif choice == "2":
            f = get_number("Enter temperature in Fahrenheit: ")
            print(f"{f:.2f} °F = {fahrenheit_to_celsius(f):.2f} °C")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
