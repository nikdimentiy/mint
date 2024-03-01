import csv

def read_students_from_csv(file_path):
    """
    Reads student information from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing student data.

    Returns:
        list: A list of dictionaries, each representing a student with keys 'name' and 'home'.
    """
    students = []

    # Open the CSV file in read mode
    with open(file_path, newline='') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Assuming each row has at least two columns: name and home
            if len(row) >= 2:
                # Add student information to the list
                students.append({"name": row[0], "home": row[1]})
            # Ensure proper handling of empty cells or malformed data
            else:
                print("Skipping malformed row:", row)

    return students

def print_students(students):
    """
    Prints student information sorted by name.

    Args:
        students (list): A list of dictionaries, each representing a student with keys 'name' and 'home'.
    """
    # Sort students alphabetically by name
    sorted_students = sorted(students, key=lambda student: student["name"])

    # Print each student's name and home
    for student in sorted_students:
        print(f"{student['name']} is from {student['home']}")

# Path to the CSV file containing student data
csv_file_path = "students1.csv"

# Read student information from the CSV file
students_data = read_students_from_csv(csv_file_path)

# Print student information sorted by name
print_students(students_data)
