import json

fp  = open('baseSet.json')
raw_api_result = json.load(fp)
jungle_set = open('jungleSet.json')
raw_api_jungle_results = json.load(jungle_set)
fossil_set = open('fossilSet.json')
raw_api_fossil_results = json.load(fossil_set)
# print(raw_api_result)
# print(raw_api_result.keys())


web_page = '<!DOCTYPE html><html><body><h1>Pokemon</h1>'

for pokemon in raw_api_result['data']:
    # print('name: '+ pokemon['name'])
    # print('image_url: '+ pokemon['images']['large'])
    # print('image_url: '+ pokemon['images']['small'])
    web_page += '<img src="'+pokemon['images']['small']+'" >'

for jungle_pokemon in raw_api_jungle_results['data']:
    web_page += '<img src="'+jungle_pokemon['images']['small']+'" >'

for fossil_pokemon in raw_api_fossil_results['data']:
    web_page += '<img src="'+fossil_pokemon['images']['small']+'" >'


web_page = web_page + '</body></html>'

print(web_page)