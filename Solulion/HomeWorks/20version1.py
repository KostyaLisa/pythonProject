def detector_name(name):

    nameUpper = name.upper()

    nameLower = name.lower()

    name_no_spaces = name.replace(" ", "")
    num_letters = len(name_no_spaces)

    first_name = name.split()[0]
    first_name_length = len(first_name)

    print(nameUpper)
    print(nameLower)
    print(num_letters)
    print(first_name_length)

name = input("Enter your name: ")
detector_name(name)