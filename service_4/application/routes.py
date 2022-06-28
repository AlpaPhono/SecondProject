from application import app
from flask import request
from random import choice

@app.route('/prize',methods = ['GET','POST'])
def prize():
    chars = request.data.decode("utf-8")
    if chars [0] == "a":
        prizes = ([50] * 3) + [100]
        prize = '£' + str(choice(prizes))
        return prize 
    else:
        return "No prize for you"
