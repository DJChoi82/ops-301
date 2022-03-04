#!/bin/bash
#Class 5 Bash Script
#DJ Choi
#3/4/2022
#Writing bash script to clear logs

#Run this script as root

#main

#declaring variable
log1=/var/log/syslog

#declaring variable
log2=/var/log/wtmp

#declaring variable
log3=/var/log/auth.log

#printing message
echo System log contents before clearing

#printing syslog contents
cat $log1

#clearing log
cat /dev/null > $log1

#priting message
echo System log contents after clearing

#printing syslog contents
cat $log1

#printing message
echo WTMP log contents before clearing

#printing wtmp log contents
cat $log2

#clearing log
cat /dev/null > $log2

#printing message
echo WTMP log contents after clearing

#printing wtmp log contents
cat $log2

#printing message
echo Auth log contents before clearing

#printing auth log contents
cat $log3

#clearing log
cat /dev/null > $log3

#printing message
echo Auth log contents after clearing

#printing auth log contents
cat $log3
#end
