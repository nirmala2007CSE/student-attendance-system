students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    students[roll_no] = {
        "name": name,
        "attendance": 0
    }
    print("Student added successfully!")

def mark_attendance():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        students[roll_no]["attendance"] += 1
        print("Attendance marked successfully!")
    else:
        print("Student not found!")

def view_students():
    if not students:
        print("No students available.")
        return

    print("\nStudent Attendance")
    print("------------------")

    for roll_no, details in students.items():
        print(
            "Roll No:", roll_no,
            "| Name:", details["name"],
            "| Attendance:", details["attendance"]
        )

while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_students()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")