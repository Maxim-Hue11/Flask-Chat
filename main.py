from flask import Flask, Response , request, render_template 
from flask_cors import CORS
import json, time, uuid

app = Flask(__name__,static_url_path='/static')

CORS(app)

# /method?argumen1=value1&argumen2=value2

users = {}

msg = []




@app.route("/")
def main():
    #  return render_template ('index.html')
    return 'comands /auth /logout /send /getall'


@app.route('/auth')
def auth():  
    new_user = request.args.get('name')
    if new_user == '' or new_user == None:
        return 'Отмена'
    if users.get(new_user) != None:
        return 'Такой пользователь уже есть'
    myuuid = uuid.uuid4()
    users[new_user]= str(myuuid)
    return str(myuuid)
    
@app.route('/logout')
def logout():
    token = request.args.get('token')
    for key, name in users.items():
        if name == token:
            del users[key]
            return 'ok' 
        return 'всё ты вышёл!!! '


@app.route('/send')
def send():
    # name = None
    text = request.args.get('message')
    token = request.args.get('token')
    print(text,token,users)
    if text == '' or text == None:
        return 'Текста нет'
    if token == '' or token == None:
        return 'Токена нет'
    
    for key, value in users.items():
        if value == token:
            return text
    return 'err'
    

    # return 'sss'        


@app.route('/getall')
def getall():
    token = request.args.get('token')
    if token not in users.values():
        return Response('Неработает', status = 403, mimetype = 'text/plain')
    x = [{
        'name': 'Ant', 'message': '', 'timestamp':123
    }]
    return Response(json.dump(x), status =200)

if __name__ == '__main__':
    print ('Rabota')
    app.run(debug=True)
     





