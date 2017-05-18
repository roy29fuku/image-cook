from django.shortcuts import render
from core.models import Book
import json

# Create your views here.
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