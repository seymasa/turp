#from .models import User, Post
from flask import Flask, request, session, redirect, url_for, render_template, flash
app = Flask(__name__)
from flask.ext.login import LoginManager, UserMixin,login_required, login_user,logout_user

@app.route('/register', methods= ['POST'])
def doLogin():
    """"    error = None
if request.method == 'POST':
       if request.form['username'] != #app.config['Username']:
           error = 'Kullanıcı Adı Yanlış'
       elif request.form['password'] != #app.config['Password']:
           error = 'Parola Yanlış'
       else:
           session['logged_in'] = True
           flash('Mis gibi giriş yaptınız :)')
           return redirect(url_for('index'))
   return render_template('login.html', error=error) """
    pass
@app.route('/login', methods= ['GET'])
def login():
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/post', methods=['POST'])
def post():
    pass

@app.route('/account-settings', methods=['GET'])
def accountSettings():
    pass

@app.route('/update-account', methods=['POST'])
def updateAccount():
    pass

@app.route('/register', methods=['POST'])
def doRegister():
    pass

@app.route('/Register', methods=['GET'])
def register():
    pass

@app.route('/<postId>/like', methods=['GET'])
def like(postId):
    pass

@app.route('/<kullaniciAdi>/follow', methods=['GET'])
def follow(kullaniciAdi):
    pass

@app.route('/<kullaniciAdi>', methods=['GET'])
def profile(kulllaniciAdi):
    pass



