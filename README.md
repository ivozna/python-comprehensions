# python-comprehensions
1. Find all of the numbers from 1–1000 that are divisible by 8
2. Find all of the numbers from 1–1000 that have a 6 in them
3. Count the number of spaces in a string (use string above)
4. Remove all of the vowels in a string (use string above)
5. Find all of the words in a string that are less than 5 letters (use string above)
6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)
7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by


# alphabet task
Write a function that:
generates a dictionary with all alphabet characters as keys,
and the number of repetitions in the sentence as values for a given sentence.

Function parameters: text

Write tests for the function:
read the sentence and the expected result from the file,
wrap the reading process with a fixture.

Example file:
“Hello, my dear friend.”, H32, e3, l2, o1,
What’s up, how are you today ?, W1, h2,…

Use fixture marker to indicate the name of the file to read.

# find matches task
1. write a function that returns sentences that are repeated in each file.

2. the list of files must be transmitted via command line arguments. 
Example: `python find_matches.py file1.txt file2.txt file3.txt`

    Print the result in the console

3. write a bash script that takes the path to the directory, finds all the text files in it, and passes them to the script above. Write the result to a file named "{directory_name (or path)} _ results.txt"

# encoding task

1. read text from input.txt file
2. read the coding map from the codes.txt file

- example map:

    blue, white, rabbit,\
    simple, triple,\
    code, name

3. replace words from the input.txt file with their codes
the code is defined as follows - {row} {column}

    example:\
    blue-00\
    triple-11\
    rabbit-02

4. write the result to the output.txt file
5. write tests

    input.txt:\
    Hello, my name is Ira. I have a rabbit\
    output.txt:\
    Hello, my name is Ira. I have a 02

6. Ensure that you run the program from the console as follows:

    `python encode.py input.txt codes.txt output.txt`

# combining files
1. Combine the content of several files into one.
2. Read the list of files to merge from the file passed as a program argument in the console.
3. Write the result to a file, the file name is the second argument from the console.
