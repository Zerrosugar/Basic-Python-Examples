def summation(a, b):
    print(a+b)
    return (a+b)


def extraction(a, b):
    print(a-b)
    return (a-b)


def divide(a, b):
    print(a/b)
    return (a/b)


def multiplication(a, b):
    print(a*b)
    return (a*b)
# This is the functions.a


operation = int(
    input("summation = 1\nextraction = 2\ndivide = 3\nmultiplication = 4\n"))
# We asked the operation.

if (operation == 1):
    a = int(input("What's a "))
    b = int(input("What's b "))
    summation(a, b)

elif (operation == 2):
    a = int(input("What's a "))
    b = int(input("What's b "))
    extraction(a, b)

elif (operation == 3):
    a = int(input("What's a "))
    b = int(input("What's b "))
    divide(a, b)

elif (operation == 4):
    a = int(input("What's a "))
    b = int(input("What's b "))
    multiplication(a, b)

else:
    print("Please, enter a defined number.")
# We did the operation using the If-Else structure.
