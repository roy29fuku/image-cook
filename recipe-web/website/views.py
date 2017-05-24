from django.shortcuts import render
from core.models import Book
import json
import pymysql.cursors

def index(request):
    return render(
        request,
        'website/index.html',
    )

def recipes(request):
    jsonScript = '''{
        "title": "にんじんにんじん",
        "ingr": [
            [
                "にんじん",
                "1本"
            ],
            [
                "塩",
                "大さじ1"
            ],
            [
                "砂糖",
                "大さじ4"
            ]
        ],
        "img": "http://hogehoge.com",
        "howto": [
            "にんじんの皮を剥きます",
            "塩をかけます"
        ]
    }'''

    data =json.loads(jsonScript)
    return render(
        request,
        'website/recipes.html',
        data,
    )


def search(S):
    # cf. search("たまねぎ")
    # json形式で返す
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='kisopro',
                                 charset='utf8',
                                 # cursorclassを指定することで
                                 # Select結果をtupleではなくdictionaryで受け取れる
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    ingr_search = "SELECT recipe_id FROM ingr WHERE name like %s"
    recipe_search = "SELECT title,imgurl,howto FROM recipe WHERE recipe_id=%s"
    get_all_ingr = "SELECT name,quantity FROM ingr WHERE recipe_id=%s"

    res = {}

    cursor.execute(ingr_search,'%'+S+'%')
    recipe_id = cursor.fetchone()["recipe_id"]

    cursor.execute(recipe_search,recipe_id)
    recipe_info = cursor.fetchone()
    res["title"] = recipe_info["title"]
    res["img"] = recipe_info["imgurl"]
    res["howto"] = list(recipe_info["howto"].split("¥;"))

    cursor.execute(get_all_ingr,recipe_id)
    recipe_ingrs = cursor.fetchall()
    res["ingr"]=[]

    for ingr in recipe_ingrs:
        res["ingr"].append((ingr["name"],ingr["quantity"]))

    jsonstring = json.dumps(res, ensure_ascii=False)

    cursor.close()
    connection.close()

    return jsonstring
