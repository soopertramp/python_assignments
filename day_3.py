""" Question - 7 : Write a Python program to display calendar? """

import calendar

# Ask the user for input
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Display the calendar
print(calendar.month(year, month))

""" Question - 8 : Write a Python program to solve quadratic equation?"""

import cmath

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Calculate the discriminant
discriminant = (b**2) - (4*a*c)

# Find the roots of the equation
root1 = (-b - cmath.sqrt(discriminant)) / (2*a)
root2 = (-b + cmath.sqrt(discriminant)) / (2*a)

# Print the roots
print(f"The roots of the equation are: {root1} and {root2}")

""" Question - 9 : Write a Python program to swap two variables without temp variable?"""

# take input from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# print the original values of x and y
print(f'Before swapping: x = {x}, y = {y}')

# swap the values of x and y using a temporary variable
temp = x
x = y
y = temp

# print the swapped values of x and y
print(f'After swapping: x = {x}, y = {y}')