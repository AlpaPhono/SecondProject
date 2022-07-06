from application import app
from flask import render_template
import requests # seperate library aside from the flask requests

@app.get('/')
def index():
    prefix = requests.get('http://service_2:5000/get_text').text
    suffix = requests.get('http://service_3:5000/get_suffix').text
    prize = requests.get('http://service_4:5000/prize', data = suffix)
    return render_template('home.html', prefix = prefix, prize = prize.text, suffix = suffix) 
