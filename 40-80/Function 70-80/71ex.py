# Create a program that has a function
# that receives a text as a parameter and that
# show a message with size
# adaptable.
#
# Ex:
# show(“Hello world.”)
# Exit:
# -=-=-=-=-=-=-=-=
# Hello World.
# -=-=-=-=-=-=-=-=


def show(text):
    length = len(text)
    print("-" * length)
    print(text)
    print("-" * length)


show("Hello world.")