import json

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

credentials["citrixCredentials"]["Value"] = []

with open('device_id.txt', 'r') as file:
    device_id = file.readlines()

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

with open('credentials.txt', 'w') as outfile:
    json.dump(credentials, outfile)
