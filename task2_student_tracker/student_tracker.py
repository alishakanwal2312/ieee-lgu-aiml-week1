
def get_student_name():
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Name cannot be empty.")


def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_integer(prompt, minimum):
    while True:
        try:
            value = int(input(prompt))

            if value >= minimum:
                return value

            print(f"Please enter a value of at least {minimum}.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F (Fail)"


def generate_report():
    print("\n===== STUDENT GRADE & ATTENDANCE TRACKER =====")

    name = get_student_name()

    roll_number = input("Enter roll number: ").strip()
    while not roll_number:
        print("Roll number cannot be empty.")
        roll_number = input("Enter roll number: ").strip()

    # Store the three subject names in a list.
    subjects = ["Python", "Mathematics", "English"]

    # Store each subject and its marks in a dictionary.
    marks = {}

    for subject in subjects:
        marks[subject] = get_marks(subject)

    average = sum(marks.values()) / len(marks)
    grade = calculate_grade(average)

    total_classes = get_integer("Enter total classes held: ", 1)
    attended_classes = get_integer("Enter classes attended: ", 0)

    while attended_classes > total_classes:
        print("Attended classes cannot exceed total classes.")
        attended_classes = get_integer(
            "Enter classes attended again: ", 0
        )

    attendance = (attended_classes / total_classes) * 100
    eligible = attendance >= 75

    # Store the complete student report in a dictionary.
    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "average": average,
        "grade": grade,
        "attendance": attendance,
        "eligible": eligible
    }

    print("\n========== STUDENT REPORT ==========")
    print(f"Name: {student['name']}")
    print(f"Roll Number: {student['roll_number']}")

    print("\nSubject Marks:")
    for subject, score in student["marks"].items():
        print(f"{subject}: {score:g}/100")

    print(f"\nAverage: {student['average']:.2f}%")
    print(f"Final Grade: {student['grade']}")
    print(f"Attendance: {student['attendance']:.2f}%")

    if student["eligible"]:
        print("Exam Eligibility: Eligible")
    else:
        print("Exam Eligibility: Not Eligible")

    print("====================================")


if __name__ == "__main__":
    generate_report()
