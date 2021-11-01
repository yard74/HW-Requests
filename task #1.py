from pprint import pprint
import requests

compared_heroes = ['Hulk', 'Captain America', 'Thanos']
intelligence = 0
smartest_hero = ''

for name in compared_heroes:
    url = 'https://superheroapi.com/api/2619421814940190/search/' + name
    response = requests.get(url)
    result = response.json()['results']
    for hero in result:
        if hero['name'] == name and int(hero['powerstats']['intelligence']) > intelligence:
            intelligence = int(hero['powerstats']['intelligence'])
            smartest_hero = hero['name']
        else:
            break
print(smartest_hero)


