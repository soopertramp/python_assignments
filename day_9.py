""" Question - 25 : Write a python program to display the multiplication table """

def generate_multiplication_table(base: int, entries: int) -> None:
    """
    This function generates a multiplication table of the given base up 
    to the given number of entries and prints it to the console.

    Args:
    - base: an integer, the base of the multiplication table
    - entries: an integer, the number of entries in the multiplication table

    Returns: None
    """
    for x in range(1, entries+1):
        print(f'{base} X {x} = {base*x}')

num = int(input('Enter the base of the multiplication table: '))
values = int(input('Enter the number of entries in the multiplication table: '))

generate_multiplication_table(num, values)

"""Question - 26 : Write a Python program to print Fibonacci sequence? """

def fibonacci_sequence(n: int) -> None:
    """
    This function prints the Fibonacci sequence up to the given number of terms.

    Args:
    - n: an integer, the number of terms in the Fibonacci sequence to print

    Returns: None
    """
    # initialize variables to hold the first two terms of the sequence
    a, b = 0, 1

    # print the first n terms of the sequence
    for i in range(n):
        print(a)
        a, b = b, a + b

# prompt the user to enter the number of terms in the sequence
n = int(input('Enter the number of terms in the Fibonacci sequence: '))

# call the fibonacci_sequence function to print the sequence
fibonacci_sequence(n)

"""Question - 27 : Write a Python program to check armstrong number?"""

def is_armstrong_number(n: int) -> bool:
    """
    This function checks whether the given number is an Armstrong number.

    Args:
    - n: an integer, the number to check

    Returns:
    - a boolean value indicating whether the number is an Armstrong number
    """
    # initialize variables
    sum = 0
    order = len(str(n))

    # calculate the sum of the cubes of the digits
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    # check if the sum is equal to the original number
    if n == sum:
        return True
    else:
        return False

# prompt the user to enter a number to check
n = int(input('Enter a number to check if it is an Armstrong number: '))

# call the is_armstrong_number function to check if the number is an Armstrong number
if is_armstrong_number(n):
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is not an Armstrong number')

"""Question - 28 : Write a Python program to find armstrong number in an interval?"""

def find_armstrong_numbers(start, end):
    # loop through each number in the interval
    for num in range(start, end + 1):
        # calculate the number of digits in the current number
        order = len(str(num))
        # calculate the sum of the cubes of the digits in the current number
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        # if the sum equals the original number, it is an Armstrong number
        if num == sum:
            print(num)

# example usage
find_armstrong_numbers(1, 1000)