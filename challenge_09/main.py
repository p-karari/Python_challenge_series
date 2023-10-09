# Question 9
# Level 2
#
# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

no_of_lines = int(input("Enter number of lines you wish to input : "))

lines = []

for n in range(no_of_lines):
    line = input("Line "+ str(n + 1) + " : ")
    lines.append(line.upper())

print(lines)


