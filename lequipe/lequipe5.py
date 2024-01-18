#! /usr/bin/python3
# par github.com/BG47510

from urllib.parse import unquote
import requests
import re
import sys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
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

#sys.argv[0] désigne le nom de fichier du script en cours d’exécution.
#sys.argv[1] [1] désigne le premier argument de ligne de commande traité par le script.
#str() utilisé avec sys.argv affiche les arguments du tableau de la ligne de commande.

result = dailymotion("https://www.dailymotion.com/player/metadata/video/k6oih7JyuEmhrnqwBZT")
print(result)
