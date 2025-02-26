import json
import os  # Import the os module

# Load the JSON file into a Python class list
def load_students(filename):
    print("Checking for file:", filename)  # Print the file name being checked
    if not os.path.exists(filename):  # Check if the file exists
        print(f"File not found: {filename}")  # Notify if the file is not found
        return []  # Return an empty list if the file does not exist
    with open(filename, 'r') as file:
        return json.load(file)

# Print each student value in the desired format
def print_students(students):
    print("This is the original Student list:")
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
    filename = 'students'  # Update this to match your actual JSON filename (without .json)
    
    # Load existing students
    students = load_students(filename)
    
    # Print original list
    print_students(students)

    # Add new student
    add_student(students, 'Doe', 'John', 12345, 'jdoe@example.com')
    
    # Print updated list
    print("\nThis is the updated Student list:")
    print_students(students)

    # Save updated list to JSON file
    save_students(filename, students)
    print("\nThe JSON file has been updated.")

# Run the program
if __name__ == "__main__":
    main()