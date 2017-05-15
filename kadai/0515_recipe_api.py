import requests
'''
https://developer.edamam.com/
'''

api_id = 'eb465fbd'
api_key = 'c750dc940c55d3433b5f33a6f7d3cd2f'
ingredient = input('検索したい食材を入力してください: ')
url = 'https://api.edamam.com/search?q='+ingredient+'&app_id='+api_id+'&app_key='+api_key
req = requests.get(url)
print(req.text)

