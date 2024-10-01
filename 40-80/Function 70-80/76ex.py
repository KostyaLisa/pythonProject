# Create a program that has a function
# which converts the temperature from Celsius
# to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F.")