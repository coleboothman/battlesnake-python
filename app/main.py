import bottle
import os


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff02',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'This year it\'s real'
    }


@bottle.post('/move')
def move():
    
     # TODO: Do things with data
    
    return {
        direction = avoid_walls()
        'move': 'direction',
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }

def getSnake():
    
    data = bottle.request.json
    our_id = 'f023067e-5411-407e-b445-04fad300ef6c'
    allsnakes = data[snakes]

    for i in range(allsnakes.len())
        curr_snake = allsnakes[i]
        if curr_snake.id == our_id
            our_snake = allsnakes[i]

    return our_snake;


def avoid_walls:

    data = bottle.request.json
    height = data[height]
    width = data[width]
    snake = getSnake()
    coordinates = snake.coordinates
    direction = ''
    boolean 
   
    if coordinates[0] == [0,0]
        direction = 'east'
    if coordinates[0] == [width, 0]
        direction = 'south'
    if coordinates[0] == [width, height]
        direction = 'west'
    if coordinates[0] == [0,height]
        direction = 'north' 
    else 
        direction = 'west'            

    return direction




    




# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
