#!/bin/python3
#Class 10 Python Script
#DJ Choi
#3/11/2022
#Writing python scripts to use conditional statements



# assigning variables
a = 70
b = 40

# main 

# using conditional statements
if  a == b: 
    print("a is equal to b")

if a != b:
    print("a does not equal to b")

if a < b:
    print("a is less than b")

if a <= b:
    print("a is less than or equal to b")

if a > b:
    print("a is greater that b")

if a >= b:
    print("a greater than of equal to b")

#using elif
if a >= b:
    print("a greater than of equal to b")
elif a < b:
    print("a is less than b")

#using elif and else
if a > b:
    print("a greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

#end



