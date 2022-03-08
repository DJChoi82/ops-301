#!/bin/bash
#Class 3 Bash Script
#DJ Choi
#3/2/2022
#Writing a bash script to change file permission in a directory

#main
#asking user for directory
echo Enter directory path
read input

#asking user for permission number
echo Enter permission number
read input2

#changing permissions
chmod -R $input2 $input

#printing directory contents and permissions
ls -l $input

#end
