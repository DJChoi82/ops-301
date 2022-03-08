#1/bin/python3
#Class 6 Python Script
#DJ Choi
#3/7/2022
#Writing python script to use bash scripts

#importing os library
import os

#declaring variable
uid = "User ID"

#calling variable
print(uid)

#declaring bash cmd
uid1 = 'whoami'

#calling bash cmd
os.system(uid1)

#declaring variable
ip = "IP info"

#calling variable
print(ip)

#declaring bash cmd
ip1 = 'ip a'

#calling bash cmd
os.system(ip1)

#declaring variable
lshw = "Hardware info"

#calling variable
print(lshw)

#declaring bash cmd
lshw1 = 'lshw -short'

#calling bash cmd
os.system(lshw1)



