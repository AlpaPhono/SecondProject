from application import app
from random import choice 

@app.route('/get_suffix', methods=['GET'])
def get_suffix():
    suffix = ["Gambit","Hero", "Menice","Badu","River","Songs","Purple","Brown",]
    text = "-".join(choice(suffix) for _ in range(1))

    return text