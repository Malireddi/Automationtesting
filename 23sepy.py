# Write a Python program which accepts a sequence of comma separated 4 digit
# binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated
# sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

binarystring=input("Enter binary nums")       
binarynums=[x for x in binarystring.split(',') if int(x,2)%5==0]
print(','.join(binarynums))

binarystring=input("Enter binary nums")
binarynums=[]
for x in binarystring.split(','):
    if(int(x,2)%5==0):
        binarynums.append(x)
print(','.join(binarynums))





# Write a Python program that accepts a sentence and calculate the number of
# letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


str = input("Enter a sentence")
digits = letters = 0
for char in str:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print("LETTERS", letters)
print("DIGITS", digits)





# Write a program which can compute the factorial of a given numbers.The
# results should be printed in a comma-separated sequence on a single
# line.Suppose the following input is supplied to the program:8
# Then, the output should be:40320

import math
n = int(input("Enter a number: "))
print(math.factorial(n))