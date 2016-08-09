import bottle


@bottle.route('/')
def index():
    my_thins = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', {
        'username': 'Pavel',
        'things': my_thins
    })


@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get('fruit')
    if not fruit:
        fruit = 'No Fruit Selected'

    bottle.response.set_cookie('fruit', fruit)
    bottle.redirect('/show_fruit')


@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie('fruit')
    return bottle.template('fruit_selection', {'fruit': fruit})

bottle.debug()
bottle.run()
