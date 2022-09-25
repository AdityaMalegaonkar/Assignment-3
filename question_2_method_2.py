# Assignment - 3

# 2. Write a Python program to reverse a string.

# 2nd method (Slicing method)

def reverse_str():
    str1 = input("Enter a string to reverse :")

    reversed_str = str1[::-1]

    print("Reversed string :", reversed_str)

reverse_str()