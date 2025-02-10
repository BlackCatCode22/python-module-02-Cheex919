# LargestOfThree.py

# 3 numbers
n1 = int(input("First number"))
n2 = int(input("Second number"))
n3 = int(input("Third number"))

#if statement / Largest number.

if n1 >= n2:
    if n1 >= n3:
        Largest = n1
    else:
        Largest = n3

else:
    if n2 >= n3:
        Largest = n2
    else:
        Largest = n3

#Result
print("The biggest number is:", Largest)

