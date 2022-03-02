#!/bin/bash
#Class 2 Bash Script
#DJ Choi
#3/1/2022
#Writing a bash script to copy syslog file to current directory and rename with current date and time
	

#assigning todays date and time to a variable
today=$(date +%Y%m%d%H%M%S)
	

#output date and time
echo "current date and time is $today (year month day hour minute second)" 
	

#copy syslog file to current directory
cp /var/log/syslog .
	

#output the file has been copied
echo syslog file has been copied to current directory
	

#assigning syslog filename to a variable
file_name=syslog
	

#assigning filename and date/time to a variable
new_filename=$file_name$today#!/bin/bash
#Class 2 Bash Script
#DJ Choi
#3/1/2022
#Writing a bash script to copy syslog file to current directory and rename with current date and time
	

#assigning todays date and time to a variable
today=$(date +%Y%m%d%H%M%S)
	

#output date and time
echo "current date and time is $today (year month day hour minute second)" 
	

#copy syslog file to current directory
cp /var/log/syslog .
	

#output the file has been copied
echo syslog file has been copied to current directory
	

#assigning syslog filename to a variable
file_name=syslog
	

#assigning filename and date/time to a variable
new_filename=$file_name$today
