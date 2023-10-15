# Question 13
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

prompt = input("Enter a sentence with letters and digits : ")
arr = [x for x in prompt.split(" ")]

# print(arr[0][0])

letter_count = 0
digit_count = 0

for word in arr:
    for letter in word:
        if letter.isalpha():
            letter_count += 1
        if letter.isdigit():
            digit_count += 1

print("LETTERS : ", letter_count)
print("DIGIT : ", digit_count)




