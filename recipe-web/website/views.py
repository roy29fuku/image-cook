from django.shortcuts import render
from core.models import Book
import random
import json
import pymysql.cursors

def index(request):
    return render(
        request,
        'website/index.html',
    )

def recipes(request):
    recipe_json = search('たまねぎ')
    context = json.loads(recipe_json)
    return render(
        request,
        'website/recipes.html',
        context,
    )


def search(S):
    # cf. search("たまねぎ")
    #
    connection = pymysql.connect(host='localhost',
                                 user='ingre',
                                 password='ingreingre',
                                 db='ingre',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    ingr_search = "SELECT recipe_id FROM ingr WHERE name like %s"
    recipe_search = "SELECT title,imgurl,howto FROM recipe WHERE recipe_id=%s"
    get_all_ingr = "SELECT name,quantity FROM ingr WHERE recipe_id=%s"

    res = {}

    cursor.execute(ingr_search,'%'+S+'%')
    recipe_ids = cursor.fetchall()
    random.shuffle(recipe_ids)
    recipe_id = recipe_ids.pop()["recipe_id"]

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
