""" Question - 29 : Write a Python Program to Find the Sum of Natural Numbers?"""

def sum_of_natural_numbers(n : int) -> int:
    """
    Calculates the sum of natural numbers up to a given input number.

    Args:
        n (int): The input number up to which to calculate the sum.

    Returns:
        int: The sum of natural numbers up to `n`.
    """
    # initialize sum and counter
    sum = 0
    i = 1

    while i <= n:
        sum += i
        i += 1

    # return the result
    return sum


""" Question - 30 : Write a Python Program to Find LCM?"""

def lcm(a: int, b: int) -> int:
    """
    Calculates the LCM (Least Common Multiple) of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The LCM of `a` and `b`.
    """
    # Find the greater number
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

""" Question - 31 : Write a Python Program to Find HCF?"""

def find_hcf(a: int, b: int) -> int:
    """
    This function takes two integers and returns their HCF (Highest Common Factor).

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The HCF of the two integers.
    """

    # find the smaller number
    if a < b:
        smaller = a
    else:
        smaller = b

    hcf = 1

    # iterate from 1 to the smaller number
    for i in range(1, smaller+1):
        if (a % i == 0) and (b % i == 0):
            hcf = i

    return hcf

# using Euclidean algorithm

def find_hcf(a: int, b: int) -> int:
    """
    This function takes two integers and returns their HCF (Highest Common Factor)
    using the Euclidean algorithm.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The HCF of the two integers.
    """

    # ensure a is greater than or equal to b
    if b > a:
        a, b = b, a

    while b != 0:
        # calculate remainder
        r = a % b

        # update a and b
        a = b
        b = r

    return a


""" Question - 32 : Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?"""

def convert_base(decimal_num: int) -> dict:
    """
    This function takes a decimal number and returns its binary, octal, 
    and hexadecimal equivalents in a dictionary.

    Args:
    decimal_num (int): The decimal number to be converted.

    Returns:
    dict: A dictionary containing the binary, octal, and hexadecimal 
    equivalents of the decimal number.
    """

    # convert decimal to binary, octal, and hexadecimal
    binary = bin(decimal_num)[2:]
    octal = oct(decimal_num)[2:]
    hexadecimal = hex(decimal_num)[2:].upper()

    # create dictionary to store results
    results = {
        'binary': binary,
        'octal': octal,
        'hexadecimal': hexadecimal
    }

    return results