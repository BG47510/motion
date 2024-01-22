#! /usr/bin/python3
# par github.com/BG47510

import requests

proxies = {
  "http": "http://45.134.79.166",
  "https": "https://143.244.57.89",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    'Accept-Language': 'fr,fr-FR;q=0.8',
    "Referer": "https://geo.dailymotion.com/"
}

def dailymotion(url):
    # Récupération des flux.
    try:
        base = s.get(url, headers=headers, proxies=proxies, timeout=15).json()
        flux = base["qualities"]["auto"][0]["url"]
        m3u8 = requests.get(flux).text
        print(m3u8)
    # Exception: si une erreur se produit lors de la récupération des flux.
    except Exception as m3u8:
        erreur = requests.get("https://raw.githubusercontent.com/BG47510/Zap/main/assets/error.m3u8").text
        print(erreur)

s = requests.Session()

result = dailymotion("https://www.dailymotion.com/player/metadata/video/x2lefik")
print(result)
