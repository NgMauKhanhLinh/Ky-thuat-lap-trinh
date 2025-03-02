import json

with open('data.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    for p in data['products']:
        print('Name: ' + p['name'])
        print('Price: ' + p['price'])
        print('Slogan: ' + p['slogan'])
        print('')

