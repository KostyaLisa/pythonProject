over_25_count = 0
men_under_17_count = 0
women_count = 0
minors_count = 0

while True:
    age = int(input("Enter age: "))
    sex = input("Enter sex (M/W): ").strip().upper()

    if sex not in ['M', 'W']:
        print("Invalid input for sex. Please enter 'M' for male or 'F' for female.")
        continue

    if age > 25:
        over_25_count += 1
    if sex == 'M' and age < 17:
        men_under_17_count += 1
    if sex == 'W':
        women_count += 1
    if age < 18:
        minors_count += 1

    continue_input = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_input != 'yes':
        break

else:
    print("Invalid input. Please enter a valid age.")

print(f"\nStatistics:")
print(f"a) Number of people over 25 years old: {over_25_count}")
print(f"b) Number of men under 17: {men_under_17_count}")
print(f"c) Number of women registered: {women_count}")
print(f"d) Number of minors registered: {minors_count}")
