import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import pymysql.cursors

def main():
    url="https://www.kyounoryouri.jp/category/l1"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    atags=soup.find_all("a")
    p=re.compile('/recipe/[0-9]{1,5}_*')

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='kisopro',
                                 charset='utf8',
                                 # cursorclassを指定することで
                                 # Select結果をtupleではなくdictionaryで受け取れる
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    recipe_ins = "INSERT INTO recipe (title, imgurl, howto) VALUES (%s, %s, %s)"
    ingr_ins = "INSERT INTO ingr (recipe_id, name, quantity) VALUES (%s, %s, %s)"
    next_id = 'SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = "kisopro" AND TABLE_NAME = "recipe"'

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
        title=title.strip()
        imgurl="https://www.kyounoryouri.jp"+recipe_contents.select_one("div.recipe--detail-main img").get("src")
        ingrs=recipe_contents.select("#ingredients_list > dl")
        ingr=[]
        for x in ingrs:
            a=x.find(class_="ingredient")
            b=x.find(class_="floatright")
            if a is None or b is None:
                continue
            ingr.append((a.text[1:],b.text))
        recipe=recipe_contents.select(".howto-sec")
        howto=[]
        for x in recipe:
            a=x.select_one(".howto-sec-val > p")
            if a is None:
                continue
            howto.append(a.text)
        proc="¥;".join(howto)

        cursor.execute(next_id)
        next_recipe_id = cursor[0]["AUTO_INCREMENT"]

        cursor.execute(recipe_ins%(title,imgurl,proc))
        connection.commit()
        for ingr_name,ingr_quantity in ingrs:
            cursor.execute(ingr_ins%(next_recipe_id,ingr_name,ingr_quantity))
            connection.commit()

        print("%s %s"%(title,imgurl))
        for x,y in ingr:
            print("%s %s"%(x,y))
        print(proc)

        break

    cursor.close()
    connection.close()


    return 0

if __name__=='__main__':
    main()