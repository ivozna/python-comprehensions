

def plus(a, b):
    return a + b


"""1. Find all of the numbers from 1 to 1000 that are divisible by 8"""

def eight_div(a, b):
    return [num for num in range(a, b) if num % 8 == 0]


"""2. Find all of the numbers from 1 to 1000 that have a 6 in them"""
def have_six(a, b):
    return [num for num in range(a, b) if '6' in str(num)]


"""3. Count the number of spaces in a string (use string above)"""
def count_spaces(text):
    return len([item for item in text if item == ' '])

"""4. Remove all of the vowels in a string (use string above)"""
def count_vowels(text):
    vowels = "aoeiu"
    return ''.join([letter for letter in text if letter not in vowels])

"""5. Find all of the words in a string that are less than 5 letters (use string above)"""
def five_letters(text):
    return ' '.join([word for word in text.split() if len(word) < 5])

"""6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)"""
def word_length(text):
    return {v:len(v) for v in text.split()}

"""7. Use a nested list comprehension to find all of the numbers 
from 1–1000 that are divisible by any single digit besides 1 (2–9)"""
def divisible(a, b):
    return [num for num in range(a, b) if any([num % el == 0 for el in range(2, 10)])]

"""8. For all the numbers 1–1000, use a nested list/dictionary comprehension 
to find the highest single digit any of the numbers is divisible by"""
def highest(a, b):
    return {num:max([el for el in range(1, 10) if num % el == 0]) for num in range(a, b) }