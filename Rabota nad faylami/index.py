import json
import pickle

# my_favourite_songs = {
#     'name': 'Alex',
#     'song': 'Summer'
# }
#
# with open('group.json', 'w', encoding='utf-8') as f:
#     json.dump(my_favourite_songs,f)
#
# with open('group.pickle','wb') as f:
#     pickle.dump(my_favourite_songs,f)

with open('group.json','r',encoding='utf-8') as f:
    result = json.load(f)
print(result)
print(type(result))

with open('group.pickle','rb') as f:
    result = pickle.load(f)
print(result)
print(type(result))