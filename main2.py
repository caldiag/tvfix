import requests

url = "http://10.105.8.1:1000/"
data = {
    "4Tredir": "http://speedtest.net/",
    "magic": "0201e145fdc7e5fa",
    "username": "cristiano.actit",
    "password": "EUmeAMO2102@"
}

response = requests.post(url, data=data)
print(response.text)  # Replace with your desired handling of the response
