""" Question - 4 : Write a Python program to swap two variables? """

a = 10
b = 20

a,b = b,a

""" Question - 5 : Write a Python program to generate a random number """

import random

random_number = random.randint(1, 100)
print(random_number) 

""" Question - 6 : Write a Python program to convert celsius to fahrenheit """

# Formula : F = (C * 1.8) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("Temperature in Fahrenheit: ", fahrenheit)

# Using function

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius temperature to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit