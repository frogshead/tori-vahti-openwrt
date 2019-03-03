#!/usr/local/bin/python3
import os
from bs4 import BeautifulSoup
import requests

response = requests.get("https://wiki.openwrt.org/toh/start")
if response.status_code == 200:
    #print("requests")
    #print(response.content)
    soup = BeautifulSoup(response.content, "html.parser")
    zipped = zip(
        soup.select('.brand'), 
        soup.select('.model'))

    for brand, model in zipped:
        cmd = "python3 /Users/mikko/ohjelmointi/github/vahti/vahti.py -p tori -q '{0} {1}'".format(model.text, brand.text)
        print(cmd)
        os.system(cmd)

    