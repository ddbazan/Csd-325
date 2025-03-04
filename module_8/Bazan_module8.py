import json
import os

# Load the JSON file into a Python list
def load_students(filename):
    print("Checking for file:", filename)
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return []
    with open(filename, 'r') as file:
        try:
            students_data = json.load(file)
            print("Loaded students data:", students_data)  # Print loaded data for debugging
            return students_data
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")
            return []

# Print each student value in the desired format
def print_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Append a new student to the list
def add_student(students, last_name, first_name, student_id, email):
    students.append({
        'L_Name': last_name,
        'F_Name': first_name,
        'Student_ID': student_id,
        'Email': email
    })

# Save updated data back to the JSON file
def save_students(filename, students):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)

# Main program
def main():
    print("Current Working Directory:", os.getcwd())  # Print the current working directory
    filename = 'students'  # Use the file name without an extension

    # Load existing students
    students = load_students(filename)

    # Print original student list
    print("\nThis is the original Student list:")
    print_students(students)

    # Add new student
    add_student(students, 'Doe', 'John', 12345, 'jdoe@example.com')

    # Print updated student list including the newly added student
    print("\nThis is the updated Student list:")
    print_students(students)

    # Save the updated list back to the JSON file
    save_students(filename, students)
    print("\nThe JSON file has been updated.")

# Run the program
if __name__ == "__main__":
    main() 