import requests
import json

# payload = {
#     'vardas': 'Jonas',
#     'pavarde': 'Jonaitis',
#     'amzius': 35
# }
# r = requests.put('http://127.0.0.1:8000/')
# # r = requests.delete('http://127.0.0.1:8000/', json=payload)
# dictionary = json.loads(r.text)
# print(dictionary)
# print(dictionary['about'])

# r2 = requests.get('http://127.0.0.1:8000/keliamieji/2020')
# print(r2.text)
# dictionary2 = json.loads(r2.text)
# print(type(dictionary2))
# # print(dictionary2['result'])




# įrašome užduotį
# nauja_uzduotis = {
#     "pavadinimas": "Nupirkti pieno",
#     "atlikta": False
# }
#
# r = requests.post('http://127.0.0.1:8000/uzduotis', json=nauja_uzduotis)
# print(json.loads(r.text))



# Nuskaitome visas užduotis
# r = requests.get('http://127.0.0.1:8000/uzduotis')
# print(json.loads(r.text))




# Nuskaitome vieną užduotį
# r = requests.get('http://127.0.0.1:8000/uzduotis/2')
# print(json.loads(r.text))



# Pakeičiame vieną užduotį
# nauja_uzduotis = {
#     "pavadinimas": "Išplauti grindis",
#     "atlikta": False
# }
#
# r = requests.put('http://127.0.0.1:8000/uzduotis/2', json=nauja_uzduotis)
# print(json.loads(r.text))



# Ištriname užduotį
# r = requests.delete('http://127.0.0.1:8000/uzduotis/1')
# print(json.loads(r.text))

