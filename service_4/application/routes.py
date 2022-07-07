from application import app
from flask import request
from random import choice
import requests

@app.route('/prize',methods = ['GET','POST'])
def prize():
    suffix = request.data.decode("utf-8")
    prefix = requests.get('http://service_2:5000/get_text').text

    rnbCombinations = ["SoulBadu","SoulSongz","LoveBadu","LoveSongz","MusicBadu","LoveSongz","BabyKeyz","BabyVibe"]
    rapCombinations = ["BabySwag","YoungVibe","YoungSwag","YoungMoney","LilVibe","LilSwag","LilMoney","LilBadu"]
    
    name =f"{prefix}{suffix}"
    if name in rnbCombinations:
        return "You could be an RNB artist"
    elif name in rapCombinations:
        return "You could be a Rap Artist"
    else:
        return "You can do any Genre!"
