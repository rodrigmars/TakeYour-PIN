from bottle import route, run
from core.pin import pin

@route('/pin/<user>')
def index(user):
    
    code = pin(user)()

    return {'pin': code}


run(debug=True, reloader=True, host='localhost', port=8080)
