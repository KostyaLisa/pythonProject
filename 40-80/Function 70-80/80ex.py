# Create a program with a function that will
# receive several notes from students and will
# return a dictionary with the following:
#
# a) Number of notes
# b) The highest score
# c) The class average
# d) The situation (optional logic)
# >12 – good
# <9.5 – weak
# >9.5 and <12 - reasonable


def calculate_grades(grades):
    count_notes = len(grades)
    highest_score = max(grades)
    class_average = sum(grades) / count_notes
    situation = "good" if class_average > 12 else "weak" if class_average < 9.5 else "reasonable"

    return {
        "count_notes": count_notes,
        "highest_score": highest_score,
        "class_average": class_average,
        "situation": situation
    }

grades = list(map(float, input('Enter the notes separated by space: ').split()))

result = calculate_grades(grades)

print(result)