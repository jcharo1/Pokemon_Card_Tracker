import json


# print(raw_api_result)
# print(raw_api_result.keys())
# web_page = '<!DOCTYPE html><html><body><h1>Pokemon</h1>'

# for pokemon in raw_api_result['data']:
#     # print('name: '+ pokemon['name'])
#     # print('image_url: '+ pokemon['images']['large'])
#     # print('image_url: '+ pokemon['images']['small'])
#     web_page += '<img src="'+pokemon['images']['small']+'" >'

# for jungle_pokemon in raw_api_jungle_results['data']:
#     web_page += '<img src="'+jungle_pokemon['images']['small']+'" >'

# for fossil_pokemon in raw_api_fossil_results['data']:
#     web_page += '<img src="'+fossil_pokemon['images']['small']+'" >'

# web_page = web_page + '</body></html>'

# print(web_page)

all_pokemon_set = open('pokemonSets/all_pokemon.json')
all_pokemon = json.load(all_pokemon_set)


# mikes_set = open('pokemonSets/all_pokemon.json')
# all_pokemon = json.load(mikes_set)

print(all_pokemon['base1-4'])

# data = get_pokemon_data('base3-1')
# print(data)
    # acess the pokemon list and interate throught the list to find pokemon id that was passed in 