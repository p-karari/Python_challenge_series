# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

raw_input = input("Enter a sentence with upper case and lower case letters : ")
raw_input = [word for word in raw_input.split(" ")]

upper_case_count = 0
lower_case_count =0

for word in raw_input:
    for letter in word:
        if letter.isupper():
            upper_case_count += 1

        if letter.islower():
            lower_case_count += 1

print("UPPER CASE ",upper_case_count)
print("LOWER CASE ",lower_case_count)