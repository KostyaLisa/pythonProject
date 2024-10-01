# Create a program that reads the name, gender and
# age of several people, keeping each
# given in a dictionary and all
# dictionaries in a list. At the end show:
#
# a) How many people were registered;
# b) What is the average age of the group;
# c) How many women were registered;
# d) How many men above average age were
# registered.

people = []

while True:
    name = input("Enter the name (or 'done' to finish): ")
    if name.lower() == "done":
        break

    gender = input("Enter the gender (Male/Female): ")
    age = int(input("Enter the age: "))

    person = {
        "name": name,
        "gender": gender,
        "age": age
    }

    people.append(person)


# a) How many people were registered
num_people = len(people)
print(f"Number of people registered: {num_people}")


# b) What is the average age of the group
total_age = sum(person["age"] for person in people)
average_age = total_age / num_people
print(f"Average age of the group: {average_age:.2f}")


# c) How many women were registered
num_women = sum(person["gender"].lower() == "female" for person in people)
print(f"Number of women registered: {num_women}")


# d) How many men above average age were registered
num_above_average_age = sum(person["age"] > average_age for person in people)
print(f"Number of men above average age registered: {num_above_average_age}")

# Optional:


# e) What is the oldest person in the group
oldest_person = max(people, key=lambda person: person["age"])
print(f"Oldest person in the group: {oldest_person['name']}")


# f) What is the youngest person in the group
youngest_person = min(people, key=lambda person: person["age"])
print(f"Youngest person in the group: {youngest_person['name']}")


# g) What is the person with the highest age
highest_age_person = max(people, key=lambda person: person["age"])
print(f"Person with the highest age: {highest_age_person['name']}")


# h) What is the person with the lowest age
lowest_age_person = min(people, key=lambda person: person["age"])
print(f"Person with the lowest age: {lowest_age_person['name']}")
