import requests
import urllib.request
from bs4 import BeautifulSoup
import re

def main():
    url="https://www.kyounoryouri.jp/category/l1"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    atags=soup.find_all("a")
    p=re.compile('/recipe/[0-9]{1,5}_*')

    for item in atags:
        link=item.get('href')
        if link is None:
            continue
        if not ('recipe' in link):
            continue
        if p.match(link):
            print(link)

    return 0

if __name__=='__main__':
    main()