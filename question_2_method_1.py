# Assignment - 3

# 2. Write a Python program to reverse a string.

# 1st method (Logical method)

def reverse_str():
    str1 = input("Enter a string to reverse :")

    reversed_str = ""
    length = len(str1)

    while length > 0:
        reversed_str += str1[length - 1]
        length = length - 1

    print("Reversed string :", reversed_str)

reverse_str()