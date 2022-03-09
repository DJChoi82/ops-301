#1/bin/python3
#Class 7 Python Script
#DJ Choi
#3/8/2022
#Writing python script to generate directory info

# Import libraries
import os

# Declaration of variables

### Read user input here into a variable
udir = input("Enter directory path:")

# Declaration of functions

### Declare a function here
def functiona(testdir):
    for (root, dirs, files) in os.walk(testdir):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main

### Pass the variable into the function here
functiona(udir)

# End
