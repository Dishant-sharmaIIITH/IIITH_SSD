from flask import Flask,request
import sqlite3  


conn = sqlite3.connect('database.db')


app=Flask(__name__)


# @app.route('/')
# def home():
#        print("hello user")


@app.route('/')
def home():
       return "hello user"
#     return render_template('notes.html')


@app.route('/user/signin')
def signin():
       return "user signin"
#     return render_template('notes.html')


@app.route('/user/signup',methods=['POST'])
def signup():
       if(request.method=='POST'):
              req=request.get_json()
              username=req['username']
              password=req['password']
              check_user=User.query.filter_by(username=username).first()
              if(check_user is not None):
                     return "already exist"
              else:
                     return "registerd successfully"



       return "user signup"
#     return render_template('signup.html')


@app.route('/user/signout')
def signout():
       return "user signout"
#     return render_template('signup.html')

if __name__=="__main__":
    app.run(debug=True)