def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B+'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    else:
        return 'F'

def generate_report_card():
    student = {}
    student['Name'] = input("Enter student name: ")
    student['Class'] = input("Enter class: ")
    student['Roll No'] = input("Enter roll number: ")

    num_subjects = int(input("Enter number of subjects: "))
    marks = {}

    for i in range(num_subjects):
        subject = input(f"Enter name of subject {i+1}: ")
        score = float(input(f"Enter marks for {subject}: "))
        marks[subject] = score

    total = sum(marks.values())
    average = total / num_subjects
    grade = calculate_grade(average)

    print("\n---------- Report Card ----------")
    print(f"Name     : {student['Name']}")
    print(f"Class    : {student['Class']}")
    print(f"Roll No  : {student['Roll No']}")
    print("\nMarks:")
    for subject, score in marks.items():
        print(f"{subject}: {score}")
    print(f"\nTotal Marks : {total}")
    print(f"Average     : {average:.2f}")
    print(f"Grade       : {grade}")
    print("---------------------------------")

    # Optional: Save to file
    save = input("Do you want to save the report? (y/n): ")
    if save.lower() == 'y':
        filename = f"{student['Name'].replace(' ', '_')}_Report.txt"
        with open(filename, 'w') as f:
            f.write("---------- Report Card ----------\n")
            f.write(f"Name     : {student['Name']}\n")
            f.write(f"Class    : {student['Class']}\n")
            f.write(f"Roll No  : {student['Roll No']}\n\n")
            f.write("Marks:\n")
            for subject, score in marks.items():
                f.write(f"{subject}: {score}\n")
            f.write(f"\nTotal Marks : {total}\n")
            f.write(f"Average     : {average:.2f}\n")
            f.write(f"Grade       : {grade}\n")
            f.write("---------------------------------\n")
        print(f"Report card saved as {filename}")

# Run the program
generate_report_card()