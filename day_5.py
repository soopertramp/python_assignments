""" Question 13 : Write a python program to reverse a string ?"""

string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

""" Question 14 : Write a python program to count the vowels in a string ?"""

# ask the user to input a string
string = input("Enter a string: ")

# define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# initialize a variable to count the number of vowels
count = 0

# loop through each character in the string
for char in string:
    # if the character is a vowel, increment the count
    if char.lower() in vowels and char.isalpha():
        count += 1

# print the count of vowels in the string
print("The number of vowels in the string is:", count)


""" Question 15 : Write a python program to count the consonants in a string ?"""

# ask the user to input a string
string = input("Enter a string: ")

# define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# initialize a variable to count the number of consonants
count = 0

# loop through each character in the string
for char in string:
    # if the character is not a vowel and is an alphabet, increment the count
    if char.lower() not in vowels and char.isalpha():
        count += 1

# print the count of consonants in the string
print("The number of consonants in the string is:", count)

#isalpha()

string = "Hello, World!"
print(string.isalpha()) 

string = "HelloWorld"
print(string.isalpha())