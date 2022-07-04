from application import app 
from random import choice

@app.route('/get_text', methods=['GET'])
def get_text():
        Prefix =["Lil","Baby","Da","Music","Soul","King","Prince","Childish","Tiny","Neo","Royal","Magic","Lyrical","Crooked","Slum","Machine","JAY","A","B"]
        text = ''.join(choice(Prefix) for _ in range(1)) 
    
        return text 
