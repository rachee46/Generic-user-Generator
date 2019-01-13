import json

#create a dictionary call credentials with the header for the json file
#and a key "citrixCredentials" with a blank dictionary as its value
credentials = {
    "serverHost": {
        "Value": "auth01.demo.gohealthcast.com"
    },
    "serverPort": {
        "Value": 443
    },
    "citrixResourceName": {
        "Value": "dgwin10"
    },
    "appMode": {
        "Value": 1
    },
    "citrixCredentials": {}
}

#Create a key in the "citrixCredentials" dictionary with "Value" as its key
# and a blank list as its value associated
credentials["citrixCredentials"]["Value"] = []

#open the device_id.txt file and create a list with each device id as separaste strings
with open('device_id.txt', 'r') as inputfile:
    device_id = inputfile.readlines()

#Update the blank list in the "citrixCredentials" dictionary  
#Each item in the lists will be a dictinary with deviceSerialNumber, username, and password as keys
#The value of deviceSerialNumber is the next item in the device_id list
#The value of username is a generic id in the format of string with "generic" and concatenated with an integer, 
#the integer starting with 1 and up to the index number of the last item in the device_id list (plus 1)
#The password is always the same
for item in device_id:
    generic_user = "generic" + str(device_id.index(item) + 1)
    credentials["citrixCredentials"]["Value"].append({
        "deviceSerialNumber":
        item.strip(),
        "username":
        generic_user,
        "password":
        "Bdltko$5"
    })

#Automatically generates the json formatted file, credentials.txt, with the value of the variable credentials
with open('credentials.txt', 'w') as outfile:
    json.dump(credentials, outfile)
