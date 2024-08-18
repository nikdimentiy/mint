"""
This script reads student data from a CSV file, where each line contains a student's name and house.
It stores the data in a list of dictionaries and then prints the students sorted by their names in reverse order.
"""

# Initialize an empty list to store student data
students = []

# Open the CSV file containing student data
with open("students.csv") as file:
    # Read each line in the file
    for line in file:
        # Split the line into name and house, removing any trailing whitespace
        name, house = line.rstrip().split(",")
        # Create a dictionary for the student
        student = {"name": name, "house": house}
        # Append the student dictionary to the students list
        students.append(student)

def get_name(student):
    """
    Function to extract the name from a student dictionary.
    
    Parameters:
    student (dict): A dictionary containing student information.
    
    Returns:
    str: The name of the student.
    """
    return student["name"]

# Sort the students list by name in reverse order and print each student's information
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

# Driver code
if __name__ == "__main__":
    # This block will only run if the script is executed directly
    print("Student List:")
    for student in students:
        print(f"{student['name']} is in {student['house']}")
