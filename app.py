import os
from bottle import route, run, template

@route('/')
@route('/<name>')
def index(name=os.getenv('NAME', 'World')):
    return template('Hello, <b>{{name}}</b>!', name=name)

run(host='0.0.0.0', port=80)
