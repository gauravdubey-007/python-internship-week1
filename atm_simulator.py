"""Mini Project (W1): Simple ATM Simulator.

Features: PIN-based login, check balance, deposit, withdraw.
Each operation is implemented as a separate function.
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3

balance = 1000.0


def login():
    """Ask for PIN. Allow up to MAX_ATTEMPTS tries. Return True if successful."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            print("Login successful!\n")
            return True
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Incorrect PIN. {remaining} attempt(s) left.")
    print("Too many wrong attempts. Card blocked.")
    return False


def get_amount(prompt):
    """Return a positive amount entered by the user, or None if invalid."""
    try:
        amount = float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return amount


def check_balance():
    print(f"Your current balance is: Rs. {balance:.2f}")


def deposit():
    global balance
    amount = get_amount("Enter amount to deposit: ")
    if amount is None:
        return
    balance += amount
    print(f"Rs. {amount:.2f} deposited successfully.")
    check_balance()


def withdraw():
    global balance
    amount = get_amount("Enter amount to withdraw: ")
    if amount is None:
        return
    if amount > balance:
        print("Insufficient balance.")
        return
    balance -= amount
    print(f"Rs. {amount:.2f} withdrawn successfully.")
    check_balance()


def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    print("===== Welcome to Simple ATM =====")
    if not login():
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
