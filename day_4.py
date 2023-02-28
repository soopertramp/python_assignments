""" Question - 10 : Write a python program to convert kilometers to miles ?"""

""" Prompt the user to enter a distance in kilometers and store it 
as a float"""
kilometers = float(input("Enter distance in kilometers: "))

# Define the conversion factor from kilometers to miles
km_in_miles = 0.621371

# Convert the distance in kilometers to miles by multiplying it by the conversion factor
miles = kilometers * km_in_miles

# Round the result to two decimal places using the built-in round() function
miles_rounded = round(miles, 2)

""" Print out the original distance in kilometers and the converted distance in miles, 
rounded to two decimal places"""
print(f"{kilometers} kilometers is equal to {miles_rounded} miles")

""" Question - 11 : Write a python program to check if a Number is positive
negative or zero?"""

def check_number(n):
    """
    This function takes a number as input and checks if it is positive, negative or zero.

    Args:
    n (int or float): The number to be checked

    Returns:
    str: A string indicating if the number is positive, negative or zero
    """

    if n > 0: # if the number is greater than 0
        return "Positive" # return 'Positive' as the number is positive
    elif n < 0: # if the number is less than 0
        return "Negative" # return 'Negative' as the number is negative
    else: # if the number is neither greater than nor less than 0, it must be 0
        return "Zero" # return 'Zero' as the number is 0

check_number(10)
check_number(-10)
check_number(0)

""" Question - 12 : Write a python program to check if a number is odd or even?""" 

def check_odd_even(num):
    """
    This function takes a number as input and checks if it is odd or even.

    Args:
    num (int): The number to be checked

    Returns:
    str: A string indicating if the number is odd or even
    """

    if num % 2 == 0: # If the number is divisible by 2
        return "Even" # return 'Even' as the number is even
    else: # if the number is not divisible by 2
        return "Odd" # return 'Odd' as the number is odd

check_odd_even(10)

check_odd_even(7)