""" Question - 19 : Write a python program to remove consonants in a string? """

def remove_consonants(string):
    """
    This function takes a string as input and returns a new 
    string that only contains vowels.
    """
    vowels = "AEIOUaeiou"
    new_string = ""
    for char in string:
        if char in vowels:
            new_string += char
    return new_string

# Get user input for the string to process
input_string = input("Enter a string: ")

# Call the remove_consonants function with the user input as input
output_string = remove_consonants(input_string)

# Print the output string
print("Output string with vowels only:", output_string)

""" Question - 20 : Write a python program to remove the alpha characters in ths string """ 

def remove_alpha(string):
    """
    This function takes a string as input and returns a new string 
    that only contains non-alphabetic characters.
    """
    new_string = ""
    for char in string:
        if not char.isalpha():  # Check if the character is not an alphabetic character
            new_string += char
    return new_string

# Get user input for the string to process
input_string = input("Enter a string: ")

# Call the remove_alpha function with the user input as input
output_string = remove_alpha(input_string)

# Print the output string
print("Output string with non-alphabetic characters only:", output_string)

""" Question - 21 : Write a python prpgram to check leap year"""

def is_leap_year(year):
    """
    This function takes a year as input and returns True if it's a leap year, 
    False otherwise.
    """
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        # If the year is divisible by 4 and not divisible by 100, or 
        # it's divisible by 400, it's a leap year
        return True
    else:
        return False

# Get user input for the year to check
input_year = int(input("Enter a year: "))

# Call the is_leap_year function with the user input as input
if is_leap_year(input_year):
    print(input_year, "is a leap year")
else:
    print(input_year, "is not a leap year")