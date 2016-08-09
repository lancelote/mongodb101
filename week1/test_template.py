import bottle


@bottle.route('/')
def index():
    my_things = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', username='Pavel', things=my_things)
    # return bottle.template('hello_world', {'username': 'Pavel'
    #                                        'things': my_things})

bottle.debug(True)
bottle.run(host='localhost', port=8080)
