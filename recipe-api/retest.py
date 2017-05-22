import re
import pymysql.cursors

def main():
    '''sql書き込みテスト'''
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


    cursor.execute(next_id)
    next_recipe_id = cursor.fetchone()["AUTO_INCREMENT"]
    #print(next_recipe_id)

    title ='たっぷり蒸し野菜アンチョビソース'
    imgurl='https://www.kyounoryouri.jp/upfile/l_1338868689_9053.jpg'
    proc='野菜はそれぞれ食べやすい大きさに切る。¥;しっかりふたのできる鍋に1を並べ、塩・オリーブ油各少々、水適量を回しかけてふたをして、弱めの中火で15分間ほどじっくり蒸し上げる。蒸し上がりの2分ほど前にトマトを加え、一緒に蒸し上げる。¥;【アンチョビソース】をつくる。鍋にオリーブ油、にんにくを入れ、弱火にかける。フツフツとしてきたらさらに火を弱め、木べらで混ぜながらにんにくが色づくまでじっくりと火にかける。バターを加え、にんにくがさらにきつね色になるまで加熱し、アンチョビを加える。木べらでほぐし、アンチョビがペースト状になって全体になじんできたら火を止め、器に盛る。¥;蒸した野菜に、温かいソースをかけながら食べる。'
    ingrs=[('トマト','1コ'),('塩','')]

    cursor.execute(recipe_ins, (title, imgurl, proc))
    connection.commit()
    for ingr_name, ingr_quantity in ingrs:
        cursor.execute(ingr_ins, (next_recipe_id, ingr_name, ingr_quantity))
        connection.commit()


    cursor.close()
    connection.close()

    return 0

if __name__=='__main__':
    main()
