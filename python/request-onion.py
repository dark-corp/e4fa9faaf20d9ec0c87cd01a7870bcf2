import requests
import json

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

site = 'your link here'

data = requests.get(site,proxies=proxies).text

print(data)
