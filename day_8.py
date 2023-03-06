""" Question - 22 : Write a python program to to check whether a number is a prime?"""

def is_prime(num):
    """
    Check if a number is a prime number.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # numbers less than or equal to 1 are not prime
    if num <= 1:  
        print(num, "is not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            # if the number is divisible by any number between 2 and sqrt(num), 
            # it's not prime
            if num % i == 0:  
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")

""" Question - 23 : Write a Python program to print all prime numbers in the interval 0f 1 - 10000?"""

def print_primes(start=1, end=10000):
    """
    Prints all prime numbers within the given interval.

    Args:
        start (int): The starting number of the interval (default is 1).
        end (int): The ending number of the interval (default is 10000).

    Returns:
        None.
    """
    for num in range(start, end + 1):
        # check if the number is greater than 1
        if num > 1:
            # check if the number is prime
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=' ')

""" Question - 24 : Write a Python program to find the factorial of a number"""

def factorial(n):
    """
    Compute the factorial of a given integer.

    Args:
        n (int): The number whose factorial to compute.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    # Check that n is non-negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Recursive case: compute factorial of n-1 and multiply by n
    else:
        return n * factorial(n-1)