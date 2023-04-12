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




# # add item
# new_item = {
#     "item_name": "car oil",
#     "price": 55,
#     "quantity": 1
# }
#
# r = requests.post('http://127.0.0.1:8000/item', json=new_item)
# print(json.loads(r.text))



# Read all items
r = requests.get('http://127.0.0.1:8000/item')
print(r.text)




# Read 1 item by id
# r = requests.get('http://127.0.0.1:8000/get_item/2')
# print(json.loads(r.text))


# Change item
# change_item = {
#         "item_name": "car oil",
#         "price": 25,
#         "quantity": 1
# }
#
# r = requests.put('http://127.0.0.1:8000/change_item/2', json=change_item)
# print(json.loads(r.text))



# Delete items
# r = requests.delete('http://127.0.0.1:8000/del_item/1')
# print(json.loads(r.text))

