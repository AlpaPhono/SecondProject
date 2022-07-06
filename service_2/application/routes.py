from application import app 
from random import choice

@app.route('/get_text', methods=['GET'])
def get_text():
        prefix =["Lil","Baby","Young","Music","Love","Soul",]
        text = ''.join(choice(prefix) for _ in range(1)) 
    
        return text 
