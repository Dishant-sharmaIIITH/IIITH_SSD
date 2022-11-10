from flask import Flask,request




@app.route('/user/signup')
def signup():
    username="dishant"
    password="123"
    payload={
        'username':username,
        'password':password
    }
    resp=request.post("http://127.0.0.1:5000/signup",json=payload).content.decode()