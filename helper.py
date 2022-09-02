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

# all_pokemon_set = open('pokemonSets/all_sets.json')
# all_pokemon = json.load(all_pokemon_set)





# # mikes_set = open('pokemonSets/all_pokemon.json')
# # all_pokemon = json.load(mikes_set)

# for x in all_pokemon:
#     if x["set"]["id"] == 'base5':
#         print(x["name"])
# data = get_pokemon_data('base3-1')
# print(data)
    # acess the pokemon list and interate throught the list to find pokemon id that was passed in 





import json

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity


# all_sets = Set.all() # a list of set


# allseries={} # organize set objs by series collections
# for x in all_sets:
#     if x.series not in allseries:
#         allseries[x.series]=[x]
#     else:
#         allseries[x.series]+=[x]


# output=[] #convert to list --

# for x in allseries:
    
#     output.append(x)


# print(len(output))





# all_sets = Set.all() # a list of set


# collections_by_series={} # organize set objs by series collections
# for set in all_sets:
#     if set.series not in collections_by_series:
#         collections_by_series[set.series]=[("name",set.name), ("symbol", set.images.symbol), ("logo",set.images.logo), ("series" , set.series),("total" , set.total),("releaseDate ", set.releaseDate)]
#     else:
#         collections_by_series[set.series].append([("name",set.name), ("symbol", set.images.symbol), ("logo",set.images.logo), ("series" , set.series),("total" , set.total),("releaseDate ", set.releaseDate)])


# output=[]


# # for k, v in collections_by_series.items:

# #     print(k, v)


# print(collections_by_series["Base"]) # #convert dict to list
# # for set in collections_by_series:
    
#     output.append(set)


# print(output[0][0])



all_sets = Set.all() # a list of set


collections_by_series={} # organize set objs by series collections
for set in all_sets:
    datadict={}
    datadict[set.name]= set.name
    datadict[set.images.symbol]= set.images.symbol
    datadict[set.images.logo]= set.images.logo
    datadict[set.series]= set.series
    datadict[set.total]= set.total
    datadict[set.releaseDate]= set.releaseDate
    if set.series not in collections_by_series:
    
        collections_by_series[set.series]=[datadict]

    else:
        collections_by_series[set.series].append([datadict])
print(collections_by_series)