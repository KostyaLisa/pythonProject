number_dict = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen', 20: 'twenty'
}


def number_to_text():
    while True:
        try:
            # Read a number from the user
            num = int(input("Enter a number between 0 and 20: "))

            # Check if the number is within the valid range
            if 0 <= num <= 20:
                # Display the number in full text
                print(f"The number you entered is: {number_dict[num]}")
                break
            else:
                print("Please enter a valid number between 0 and 20.")
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 20.")


# Call the function
number_to_text()