from pymongo import MongoClient
import json
client = MongoClient('mongodb://localhost:27017/')
db = client.Music
collection=db.MusicInfoSorted
cursor = collection.find()
message = 'topMusics = [\n'
f=open('E:\\topSongInfo.md','w')
for song in cursor:
    message += '    ["'+song['name']+'",'+ str(song['commentTotals']*1.0/1000)+'],\n'
message += ']'
f.write(message.encode('utf-8'))
f.close()
