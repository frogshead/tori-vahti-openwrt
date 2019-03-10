#!/usr/local/bin/python3
import os
from bs4 import BeautifulSoup
import requests
import vahti
from parsers import tori

response = requests.get("https://wiki.openwrt.org/toh/start")
if response.status_code == 200:
    #print("requests")
    #print(response.content)
    soup = BeautifulSoup(response.content, "html.parser")
    zipped = zip(
        soup.select('.brand'), 
        soup.select('.model'),
        soup.select('.version'),
        soup.select('.supported_current_rel'),
        soup.select('.device_page '),
        #soup.select('.device_tech_data'),
        )


    v = vahti.Vahti()
    #v.clear_db()
    v.queries = "Raspberry Pi"
    v.parser = tori.ToriParser()
    v.main()

 #version, , , 
    for brand, model,version,supported_current_rel,device_page in zipped:
        if supported_current_rel.text == '18.06.1':
            v.queries = '{0} {1}'.format(brand.text, model.text)
            print(v.queries)
            v.parser = tori.ToriParser()
            v.main()

    