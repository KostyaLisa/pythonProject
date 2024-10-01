# Create a program that has a function
# which will take as a parameter the year of
# birth of a person and who returns
# if the person can already get the license
# driving, if you need authorization from the
# guardian or if you cannot.
#
# +18 years old – can
# -16 years old – cannot
# -18 and +16 – with authorization
import datetime


def check_license_age(year_of_birth):
    data = datetime.time
    current_year = data.year
    age = current_year - year_of_birth

    if age >= 18:
        return "Can get the license driving"
    elif age < 16:
        return "Cannot get the license driving"
    else:
        return "With authorization from the guardian"

year_of_birth = int(input("Year of Birth: "))
print(check_license_age(year_of_birth))