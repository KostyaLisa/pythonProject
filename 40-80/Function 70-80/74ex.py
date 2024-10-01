# Create a program that has a function
# that receives the name of a student and a
# list of your notes. He must calculate
# the student's average and show on the screen the
# student's name, their average and whether they
# was approved or not.


def calculate_average(name, notes):
    average = sum(notes) / len(notes)

    if average >= 7:
        print(f"{student_name} was approved with an average of {average:.1f}")
        print("Congratulations!")
    else:
        print(f"{student_name} was not approved with an average of {average:.1f}")
        print("Please, try again next time.")

student_name = input('Student Name: ')
student_notes  = list(map(float, input('Enter the notes separated by space: ').split()))
calculate_average(student_name, student_notes)
