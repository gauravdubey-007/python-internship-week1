"""Student Grade Calculator: take marks, calculate average and assign a grade."""


def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F (Fail)"


def get_marks(subject_number):
    """Keep asking until the user enters marks between 0 and 100."""
    while True:
        try:
            marks = float(input(f"Enter marks for subject {subject_number} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_subject_count():
    while True:
        try:
            n = int(input("How many subjects? "))
            if n > 0:
                return n
            print("Please enter at least 1 subject.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ").strip() or "Student"
    count = get_subject_count()

    marks = [get_marks(i) for i in range(1, count + 1)]

    total = sum(marks)
    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n--- Result ---")
    print(f"Name    : {name}")
    print(f"Total   : {total:.2f} / {count * 100}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")


if __name__ == "__main__":
    main()
