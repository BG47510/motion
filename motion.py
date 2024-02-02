#!/usr/bin/python3

import requests
import sys

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Referer": "http://s2.callofliberty.fr/"
}

erreur = requests.get("https://raw.githubusercontent.com/BG47510/Zap/main/assets/error.m3u8").text

s = requests.session()
s
def snif(url):
    lien = s.get(url, headers=headers).text
    flux = lien.replace("http://s2.callofliberty.fr/HLS-AES/", "")
   # print(flux)
    if lien.status_code == 200:
        print(flux)
    else:
        print(erreur)


m3u8 = snif(str(sys.argv[1]))
print(m3u8)

