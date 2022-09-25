# Assignment - 3

# 3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_fun():
    str1 = input("Enter a string :")
    upper_case = 0
    lower_case = 0

    for i in str1:
        if i.isupper():
            upper_case +=1
        if i.islower():
            lower_case += 1

    print("Number of upper case letters :", upper_case)
    print("Number of lower case letters :", lower_case)

string_fun()