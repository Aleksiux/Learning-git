import requests
import json

# payload = {'vardas': 'Donatas', 'pavarde': 'Noreika', 'amzius': 2000}
# r = requests.post('http://127.0.0.1:5000/', json=payload)
# dictionary = json.loads(r.text)
# print(dictionary)
#
# # {'you sent': {'amzius': 2000, 'pavarde': 'Noreika', 'vardas': 'Donatas'}}

r2 = requests.get('http://127.0.0.1:5000/leap/year:2023')
dictionary2 = json.loads(r2.text)
print(dictionary2['result'])
