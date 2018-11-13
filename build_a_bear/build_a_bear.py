import json

from flask import (Flask, render_template, redirect, url_for, request,
                    make_response, flash)

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = "akdjfn;kdm34ula8u38ur3bnbljk180"

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data

@app.route('/')
def index():
    data = get_saved_data()
    return render_template("index.html", saves=get_saved_data()) #saves is a json.loads creates a dict object that gets passed to index.html and used by it

@app.route('/builder')
def builder():
    return render_template('builder.html',
                            saves=get_saved_data(),
                            options=DEFAULTS)

@app.route('/save', methods=['POST'])
def save():
    flash("Alright! That looks awesome!")
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response

app.run(debug=True, host='0.0.0.0', port=8000)