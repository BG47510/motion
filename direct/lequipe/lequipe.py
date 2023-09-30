#!/usr/bin/python3
# par github.com/BG47510
import requests

url = f"https://www.dailymotion.com/player/metadata/video/x2lefik"
response = requests.get(url).json()
flux = response["qualities"]["auto"][0]["url"]
m3u8 = requests.get(flux).text
print(m3u8)

