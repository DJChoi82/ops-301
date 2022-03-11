#class 8 powershell script
#DJ Choi
#3/9/2022
#writing powershell script to add user to AD

#main

#add user
New-ADUser -Name "Franz Ferdinand" -Title “TPS Reporting Lead” -Company “GlobeX USA” -Office “Springfield, OR” -Department “TPS Department” -EmailAddress “ferdi@GlobeXpower.com”

#end