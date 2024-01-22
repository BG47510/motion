#! /usr/bin/python3
# par github.com/BG47510

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    'Accept-Language': 'fr,fr-FR;q=0.8',
    "Referer": "https://www.lequipe.fr/tv/"
}

def dailymotion(url):
    # Récupération des flux.
    try:
        base = s.get(url, headers=headers, timeout=15).json()
        flux = base["qualities"]["auto"][0]["url"]
        m3u8 = requests.get(flux).text
        print(m3u8)
    # Exception: si une erreur se produit lors de la récupération des flux.
    except Exception as m3u8:
        erreur = "https://raw.githubusercontent.com/BG47510/Zap/main/assets/error.m3u8"
        m3u8 = requests.get(erreur).text
        print(m3u8)

s = requests.Session()

result = dailymotion("https://www.dailymotion.com/player/metadata/video/x2lefik")
print(result)
