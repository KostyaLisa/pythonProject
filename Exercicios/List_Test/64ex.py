# Create a program that reads the name and
# average of a student, calculating their
# situation, all within a dictionary.
# At the end, show all the content of the
# dictionary.
#
# Situation:
# Average >= 9.5 – Approved
# Average < 9.5 - Failed


students = {} # Dictionary to store student information
while True:  # Get
    name = input("Enter the name of the student (or 'done' to finish): ")
    # Break loop if user enters 'done'
    if name.lower() == "done":
        break
    # Get average of the student
    average = float(input("Enter the average of the student: "))
    # Calculate the situation based on the average
    if average >= 9.5:
        situation = "Approved"
    else: # If average is less than 9.5, set the situation as 'Failed'
        situation = "Failed"

    students[name] = {"average": average, "situation": situation} # Add student information to the dictionary
     # Print the student information
    print(f"{name} - Average: {average:.1f}, Situation: {situation}")


# Print all students' information in the dictionary'
print("\nAll students' information:")
for name, data in students.items():  # Loop through the dictionary items (students)
    print(f"{name}: Average - {data['average']:.1f}, Situation - {data['situation']}") # Print student's information'


