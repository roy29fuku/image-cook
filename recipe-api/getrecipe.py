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
    mp={}

    for item in atags:
        link=item.get('href')
        if link is None:
            continue
        if not ('recipe' in link):
            continue
        if not p.match(link):
            continue
        r=requests.get("https://www.kyounoryouri.jp"+link).text
        recipe_contents=BeautifulSoup(r,'lxml')
        title=recipe_contents.find("h1",attrs={"class":"ttl"}).text
        imgurl="https://www.kyounoryouri.jp"+recipe_contents.select_one("div.recipe--detail-main img").get("src")
        ingrs=recipe_contents.select("#ingredients_list > dl")
        ingr=[]
        for x in ingrs:
            a=x.find(class_="ingredient")
            b=x.find(class_="floatright")
            if a is None or b is None:
                continue
            ingr.append((a.text,b.text))
        recipe=recipe_contents.select(".howto-sec")
        howto=[]
        for x in recipe:
            a=x.select_one(".howto-sec-val > p")
            if a is None:
                continue
            howto.append(a.text)
        break #これ外すと全部取る

    print("%s %s"%(title,imgurl))
    for x,y in ingr:
        x=x[1:]
        print("%s %s"%(x,y))
    for x in howto:
        print(x)


    return 0

if __name__=='__main__':
    main()