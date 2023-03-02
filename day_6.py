""" Question - 16 : Write a python program to count the special characters in string?"""

# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize a variable to keep track of the number of special characters
count = 0

# Loop through each character in the string
for char in string:
    # Check whether the character is not alphanumeric and not a space
    if not char.isalnum() and char != " ":
        # If the character is a special character, increment the count variable
        count += 1

# Print the number of special characters found
print("There are", count, "special characters in the string.")

""" Question - 17 : Write a python program to count the number in string?"""

# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize a variable to keep track of the number of digits
count = 0

# Loop through each character in the string
for char in string:
    # Check whether the character is a digit or a decimal point
    if (char.isdigit() or char == '.'):
        # If the character is a digit or a decimal point, increment the count variable
        count += 1

# Print the number of digits found
print("There are", count, "digits (including decimals) in the string.")

""" program that should correctly count the number of numbers 
(including decimals) in the input string:"""

# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize a variable to keep track of the number of numbers
count = 0

# Flag to indicate whether we're currently processing a number
processing_number = False

# Loop through each character in the string
for char in string:
    # Check whether the character is a digit or a decimal point
    if char.isdigit() or char == '.':
        # If we're not currently processing a number, set the flag and increment the count
        if not processing_number:
            processing_number = True
            count += 1
    # If the character is not a digit or a decimal point, reset the flag
    else:
        processing_number = False

# Print the number of numbers found
print("There are", count, "numbers (including decimals) in the string.")

""" Another Way """

string = input("Enter a string: ")
count = 0
i = 0
while i < len(string):
    # If the current character is a digit or a decimal point, check the following characters
    if string[i].isdigit() or string[i] == '.':
        j = i + 1
        while j < len(string) and (string[j].isdigit() or string[j] == '.'):
            j += 1
        count += 1
        i = j
    else:
        i += 1
print("There are", count, "numbers in the string.")

""" This program uses a while loop to iterate through the string. At each position in the string, 
it checks whether the current character is a digit or a decimal point. If it is, 
it looks ahead in the string to find the end of the current number (i.e., the next character that
is not a digit or a decimal point), and increments the count of numbers found. 
If the current character is not a digit or a decimal point, the program simply 
moves on to the next character.

With this program, if you input as5cd5.8as7, the output will indicate that there 
are 3 numbers in the string."""

""" Question - 18 : Write a python program to remove the vowels in a string? """

# Prompt the user to enter a string
string = input("Enter a string: ")

# Define the vowels that need to be removed
vowels = "aeiouAEIOU"

# Create an empty string that will store the modified string
new_string = ""

# Loop through each character in the input string
for char in string:
    # Check whether the character is a vowel
    if char not in vowels:
        # If the character is not a vowel, add it to the new string
        new_string += char

# Print the modified string without vowels
print("String with vowels removed:", new_string)