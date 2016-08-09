from pymongo import MongoClient

# Connect to database
connection = MongoClient('0.0.0.0', 32768)

db = connection.video

# Handle to names collection
movies = db.movies

item = movies.find_one()

print(item['title'])
