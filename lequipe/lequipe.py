#! /usr/bin/python3
# par github.com/BG47510

import requests
import sys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Referer": "https://www.lequipe.fr/tv/"
}

# idvideo : L'ID de la vidéo Dailymotion.
def dailymotion(idvideo):
    # Récupère les flux Dailymotion en fonction de l'ID vidéo.
    try:
        url = f"https://www.dailymotion.com/player/metadata/video/{idvideo}"
        response = s.get(url, headers=headers, timeout=15).json()
        flux = response["qualities"]["auto"][0]["url"]
        m3u8 = requests.get(flux).text
        print(m3u8)
    # Exception: si une erreur se produit lors de la récupération des flux.
    except Exception as m3u8:
        m3u8 = "https://raw.githubusercontent.com/BG47510/Zap/main/assets/error.m3u8"
        print(m3u8)

s = requests.Session()

if (sys.argv[1] == 'lequipe'):
    idvideo = 'x2lefik'
#elif (sys.argv[1] == 'lequipe1'):
#    idvideo = 'k1kypsRZF9plQhqwBRS'
#elif (sys.argv[1] == 'lequipe2'):
   # idvideo = 'k5TgcOKBUTM2KnqwBWC'
#elif (sys.argv[1] == 'lequipe3'):
#    idvideo = 'k5s40USR9HxnG5aCf1y'
#elif (sys.argv[1] == 'lequipe4'):
  #  idvideo = 'kXRfcKHV9HhcZuqwBYP'
#elif (sys.argv[1] == 'lequipe5'):
   # idvideo = 'k6oih7JyuEmhrnqwBZT'
else:
    sys.exit(1)

dailymotion(idvideo)
