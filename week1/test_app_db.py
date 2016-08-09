import bottle
import pymongo


# Handler for the default path of the web server
@bottle.route('/')
def index():
    # Connect to the MongoDB
    connection = pymongo.MongoClient('0.0.0.0', 32768)

    # Attach to the database
    db = connection.video

    # Get handle for movies collection
    movies = db.movies

    # Find a single document
    item = movies.find_one()

    return '<b>Movie: {}</b>'.format(item['title'])

bottle.run(host='localhost', port=8082)
