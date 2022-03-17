#!/bin/python3
#Class 13 Python Script
#DJ Choi
#3/16/2022
#Writing python script to use requests

#importing requests library
import requests

#main

#asking for input and assining it to a variable
inputa = input("Enter URL:")

#printing a menu
print("HTTP methods:")
print("1: get")
print("2: post")
print("3: put")
print("4: delete")
print("5: head")
print("6: patch")
print("7: options")

#asking for input and assining it to a variable
inputb = input("Select HTTP method. Enter number:")

#assigning input number to method
if inputb == "1":
    var1 = "get"
if inputb == "2":
    var1 = "post"
if inputb == "3":
    var1 = "put"
if inputb == "4":
    var1 = "delete"
if inputb == "5":
    var1 = "head"
if inputb == "6":
    var1 = "patch"
if inputb == "7":
    var1 = "options"

#assigning the different request methods to a variable
req1 = requests.get(inputa)
req2 = requests.post(inputa)
req3 = requests.put(inputa)
req4 = requests.delete(inputa)
req5 = requests.head(inputa)
req6 = requests.patch(inputa)
req7 = requests.options(inputa)

#printing what method to what url
print("Sending a", var1, "request to", inputa)

#asking if user wasts to continue. printingrequest status    
while True:
    inputc = input("Do You Want To Continue? [y/n]")
    if inputc == "y":
        if inputb == "1":
            if req1.status_code == 200:
                print("Success")
            elif req1.status_code == 404:
                print("Site not found")

        elif inputb == "2":
            if req2.status_code == 200:
                print("Success")
            elif req2.status_code == 404:
                print("Site not found")

        elif inputb == "3":
            if req3.status_code == 200:
                print("Success")
            elif req3.status_code == 404:
                print("Site not found")

        elif inputb == "4":
            if req4.status_code == 200:
                print("Success")
            elif req4.status_code == 404:
                print("Site not found")

        elif inputb == "5":
            if req5.status_code == 200:
                print("Success")
            elif req5.status_code == 404:
                print("Site not found")

        elif inputb == "6":
            if req6.status_code == 200:
                print("Success")
            elif req6.status_code == 404:
                print("Site not found")

        elif inputb == "7":
            if req7.status_code == 200:
                print("Success")
            elif req7.status_code == 404:
                print("Site not found")
        break
    
    elif inputc == "n":
        break


#response header information
response = requests.head(inputa)
print("Response header:")
print(response.headers)

#sending get request to webserver
webserver = requests.get("http://10.0.2.5/")
print(webserver.status_code)


#end



