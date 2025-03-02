import json
import os  # Import the os module for checking the working directory

# Load the JSON file into a Python list
def load_students(filename):
    print("Checking for file:", filename)  # Print the file name being checked
    if not os.path.exists(filename):  # Check if the file exists
        print(f"File not found: {filename}")  # Notify if the file is not found
        return []  # Return an empty list if the file does not exist
    with open(filename, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")
            return []  # Return an empty list if there is an error

# Print each student value in the desired format
def print_students(students):
    if not students:  # Check if students list is empty
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
    filename = 'students.json'  # Ensure this matches your actual JSON filename

    print("Current Working Directory:", os.getcwd())  # Print the current working directory

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