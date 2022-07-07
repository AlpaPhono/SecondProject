from application import app
from flask import request
from random import choice
import requests

@app.route('/genre',methods = ['GET','POST'])
def genre():
    datasent = request.get_json()
    prefix = datasent['prefix']
    suffix = datasent['suffix']
  

    rnbCombinations = ["SoulBadu","SoulSongz","LoveBadu","LoveSongz","MusicBadu","LoveSongz","BabyKeyz","BabyVibe"]
    rapCombinations = ["BabySwag","YoungVibe","YoungSwag","YoungMoney","LilVibe","LilSwag","LilMoney","LilBadu"]
    
    name =f"{prefix}{suffix}"
    if name in rnbCombinations:
        return "You could be an RNB artist"
    elif name in rapCombinations:
        return "You could be a Rap Artist"
    else:
        return "You can do any Genre!"


