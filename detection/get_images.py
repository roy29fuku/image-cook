import urllib.request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


'''
bingの画像検索から取ってくる
'''
qs = [
    'carrot',
    'onion',
    'radish',
    'tomato',
    'cabbage',
]

azure_id = 'b588d68f-d1cd-49df-9d12-ab23240b7c8d'
azure_key = 'nfO3Wotbs4CIaRt3aT+Anv1zTTBIXy4oxhGqdiAUBl4'
images_dir = 'images/'


for q in qs:
    print(q)
    html = open('urls/'+q+'.html')
    soup = BeautifulSoup(html, "lxml")
    links = soup.find_all("img", class_='rg_ic')
    count = 0
    for link in links:
        count += 1
        print(link)
        link_url = link.get("src")
        if not link_url:
            link_url = link.get("data-src")
        if not link_url:
            continue
        file_name = q + '-google-' + str(count)
        image = urllib.request.urlopen(link_url)
        image_file = open(images_dir + q + '/' + file_name + '.jpg', 'wb')
        image_file.write(image.read())
        image_file.close()
