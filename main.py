import requests
from time import sleep

url = "https://fast.net/"
request = requests.get(url, verify=False)
magic = request.text[91:107]
request_2 = requests.get(f"https://10.105.8.1:1003/fgtauth?{magic}", verify=False)
print(f'got {magic}')

username = input("input username")
password = input("input password")

data = {
    "4Tredir": "https://fast.net",
    "magic": magic,
    "username": username,
    "password": password
}



post_url = "http://10.105.8.1:1000"

req = requests.post(post_url, data=data)
