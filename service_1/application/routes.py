from application import app
from flask import render_template
import requests # seperate library aside from the flask requests

@app.get('/')
def index():
    chars = requests.get('http://service_2:5000/get_text').text
    prize = requests.get('http://service_4:5000/prize', data = chars)
    return render_template('home.html', chars = chars, prize = prize.text) 
