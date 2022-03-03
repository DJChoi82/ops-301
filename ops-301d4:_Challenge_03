#!/bin/bash
#Class 4 Bash Script
#DJ Choi
#3/3/2022
#Writing bash script with a list of options

#main

#creating a loop
for (( ; ; ))
do

#printing a list of options
echo "Option list"
echo "1) Hello world (prints "Hello world!" to the screen)"
echo "2) Ping self (pings this computer's loopback address)"
echo "3) IP info (print the network adapter information for this computer)"
echo "4) Exit"
echo "Please enter an option number"

#reading input
read input
echo ""

#if input is 1 printing hello world
if [[ "$input" == "1" ]]; then
   echo Hello world!
fi

#if input is 2 pinging loopback address
if [[ "$input" == "2" ]]; then
   ping 127.0.0.1
fi

#if input is 3 printing network card info
if [[ "$input" == "3" ]]; then
   lshw -C network
fi

#if input is 4 quitting loop and printing bye
if [[ "$input" == "4" ]]; then
   echo Bye!
   exit 0
fi

#if input is not 1-4 then printing wrong input
if [[ "$input" -gt "4" ]]; then
   echo Wrong input
fi
echo ""
done
#end
