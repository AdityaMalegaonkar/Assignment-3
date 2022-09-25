# Assignment - 3

# 1. Write a Python function to sum all the numbers in a list.

def sum_list():
    size = int(input("Enter the size of list :"))
    lst = []

    for i in range(size):
        element = int(input("Enter a number :"))
        lst.append(element)
        sum = 0
        for j in lst:
            sum += j

    print("Sum of all elements of list is :", sum)

sum_list()