import sys
import pymongo

connection = pymongo.MongoClient('0.0.0.0', 32768)

db = connection.test
users = db.users

doc = {'first_name': 'Pavel', 'last_name': 'Karateev'}

print(doc)
print('About to insert new document')

try:
    users.insert_one(doc)
except Exception as e:
    print('Insert failed:', e)

print(doc)
print('Inserting again')


try:
    users.insert_one(doc)
except Exception as e:
    print('Second insert failed:', e)
