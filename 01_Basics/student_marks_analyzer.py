
students = int(input("Enter the number of students: "))

marks = []
for i in range(students):
    marks.append(int(input("Enter marks: ")))


def calculate_average(marks):
    return sum(marks) / len(marks)


def minimum_marks(marks):
    return min(marks)


def maximum_marks(marks):
    return max(marks)


def pass_fail(marks):
    passed = 0
    failed = 0

    for mark in marks:
        if mark >= 40:
            passed += 1
        else:
            failed += 1

    return passed, failed


def grade(marks):
    A = 0
    B = 0
    C = 0
    F = 0

    for mark in marks:
        if mark >= 90 and mark <= 100:
            A += 1
        elif mark >= 75 and mark <= 89:
            B += 1
        elif mark >= 40 and mark <= 74:
            C += 1
        else:
            F += 1

    return A, B, C, F


def print_report(marks):
    print("\n========== STUDENT REPORT ==========\n")
    print("Total Students:", len(marks))
    print("Average Marks:", round(calculate_average(marks), 2))
    print("Highest Marks:", maximum_marks(marks))
    print("Lowest Marks:", minimum_marks(marks))

    passed, failed = pass_fail(marks)
    print("Passed:", passed)
    print("Failed:", failed)

    A, B, C, F = grade(marks)
    print("\nGrade Distribution")
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("F:", F)


print_report(marks)
