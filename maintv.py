import requests, getpass, os, sys
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

print("starting tvfix")

url = "https://fast.net/"
request = requests.get(url, verify=False)
magic = request.text[91:107]
request_2 = requests.get(f"https://10.105.8.1:1003/fgtauth?{magic}", verify=False)
print(f'got {magic}')

data = {
    "4Tredir": "https://fast.net",
    "magic": magic,
    "username": sys.argv[1],
    "password": sys.argv[2]
}

post_url = "http://10.105.8.1:1000"

req = requests.post(post_url, data=data)
