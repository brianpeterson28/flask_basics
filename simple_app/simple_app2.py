from flask import Flask 
from flask import request

app = Flask(__name__)

#Views must return strings! Always have to worry about data conversion. 

"""
Don't necessarily have to use request.args.get

Can make a generic call in the route directions that gets fed into 
view function. 

Treehouse is a default name that gets used if nothing is passed in. 
"""

@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
    return "Hello from {}".format(name)

"""
One view can have many routes. 
Flask will automatically check to see if any combination for the given
request string work.
"""

@app.route('/add/<int:num1>/<int:num2>')             
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1 + num2)

app.run(debug=True, port=8000, host='0.0.0.0')