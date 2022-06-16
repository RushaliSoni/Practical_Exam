import json

with open('test.json','r') as file:
    json_data = json.load(file)

for info in json_data:
    print(info)

