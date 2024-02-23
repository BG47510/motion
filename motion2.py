#! /usr/bin/python3
# par github.com/BG47510
import requests
import sys

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Referer": "https://geo.dailymotion.com",
    "visitorCountry":"FR"
}

erreur = requests.get("https://raw.githubusercontent.com/BG47510/Zap/main/assets/error.m3u8").text

s = requests.session()

def snif(url):
    try:
        source = s.get(url, headers=headers)
        base = (source).json()
        lien = base["qualities"]["auto"][0]["url"]
        m3u8 = requests.get(lien).text
    except Exception as e:
        m3u8 = erreur
    finally:
        print(m3u8)

clic = snif(sys.argv[1])
        
