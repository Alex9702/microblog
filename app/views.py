from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Edgar' } # fake user
    return render_template("index.htm",
        title = 'Home',
        user = user)
