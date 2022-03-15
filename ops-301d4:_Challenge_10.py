#!/bin/python3
#Class 11 Python Script
#DJ Choi
#3/14/2022
#Writing python script to use pythons file handling

#import libraries
import os

#main

#creates a new file
file = open("ops301_11.txt", "w")

#write lines to file
file.write("This is line 1" + os.linesep)
file.write("This is line 2" + os.linesep)
file.write("This is line 3")

#cloase file
file.close()

#opens file
file = open("ops301_11.txt", "r")

#assigning variable to the lines in the file
lines = file.readlines()

#printing line 1 in file
print(lines[0])

#delete file
os.remove("ops301_11.txt")

#end
