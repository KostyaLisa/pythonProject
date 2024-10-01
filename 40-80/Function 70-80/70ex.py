#
# Create a program that has a function
# call area() that receives the dimensions
# of a piece of land and show the area of ​​the
# land.


def area(length, width):
    return length * width

length = float(input("Enter the length of the land: "))
width = float(input("Enter the width of the land: "))

print(f"The area of the land is {area(length, width)} square meters.")
