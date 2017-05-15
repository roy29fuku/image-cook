import requests
'''
https://developer.edamam.com/
'''

api_id = 'eb465fbd'
api_key = 'c750dc940c55d3433b5f33a6f7d3cd2f'
q = input('検索したい食材を入力してください: ')
url = 'https://api.edamam.com/search?q='+q+'&app_id='+api_id+'&app_key='+api_key
response = requests.get(url).json()
recipe = response['hits'][0]['recipe']
label = recipe['label']
ingredients = recipe['ingredients']
url = recipe['url']
print('タイトル: ', label)
for ingredient in ingredients:
    print('食材: ', ingredient['text'])
print('URL: ', url)

