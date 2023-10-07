# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

x = int(input("Enter number of items you wish to add : "))
list_ = []
tuple_ = ()

print("Enter list items")
for i in range(1, (x + 1)):
    list_items = input(" ")
    list_.append(list_items)


print("List : ", list_)
print("Tuple : ", tuple(list_))
