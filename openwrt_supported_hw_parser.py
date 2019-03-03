#!/usr/local/bin/python3
import subprocess
import os
from bs4 import BeautifulSoup

with open("Table of Hardware [OpenWrt Wiki].html") as f:
    data = f.read()
    soup = BeautifulSoup(data, "html.parser")
 


for brand, model  in zip(
    soup.select('#dokuwiki__content > div > div.page.group > div > div.table.dataaggregation > table > tbody > tr > td:nth-of-type(3) '), 
    soup.select('#dokuwiki__content > div > div.page.group > div > div.table.dataaggregation > table > tbody > tr > td:nth-of-type(2)')):
    cmd = "python3 /Users/mikko/ohjelmointi/github/vahti/vahti.py -p tori -q '{0} {1}'".format(model.text, brand.text)
    print(cmd)
    os.system(cmd)
    #subprocess.call(cmd)
    #print("{0} {1}".format(model.text, brand.text)) 