#!/usr/local/bin/python3
import os
from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('https://wiki.openwrt.org/toh/start') as response:
    data = response.read()
    soup = BeautifulSoup(data, "html.parser")

    for brand, model  in zip(
        soup.select('#dokuwiki__content > div > div.page.group > div > div.table.dataaggregation > table > tbody > tr > td:nth-of-type(3) '), 
        soup.select('#dokuwiki__content > div > div.page.group > div > div.table.dataaggregation > table > tbody > tr > td:nth-of-type(2)')
        ):
        print("test")
        cmd = "python3 /Users/mikko/ohjelmointi/github/vahti/vahti.py -p tori -q '{0} {1}'".format(model.text, brand.text)
        print(cmd)
        os.system(cmd)
