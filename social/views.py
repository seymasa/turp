#from .models import User, Post
from flask import Flask, request, session, redirect, url_for, render_template, flash, send_from_directory
from flask_login import LoginManager, UserMixin,login_required, login_user,logout_user
from .models import User, Post # User modelini import ettik

app = Flask(__name__)



@app.route('/login', methods= ['POST'])
def doLogin():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        print(username, "-", password)
        print(User(username).login_check(password))

        if not User(username).login_check(password):
            error = 'Şifre hatalı!'

        elif not User(username).login_use(username):
            error = 'Kullanıcı adı hatalı!'
        else:
            session['username'] = username
            flash("LOGGEND IN.")
            print("Giriş Yapıldı", username)
            return redirect(url_for("homepage"))
    return render_template('login.html', error=error)



@app.route('/register', methods=['POST'])
def doRegister(): # Kayıt ol formu gönderince burası çağırılıyor
    errors       = None
    name = request.form['name']
    username     = request.form['username']
    email        = request.form['email']
    password     = request.form['password']
    confirm      = request.form['confirm']

    if(password != confirm):
        errors = "Parola ve parola tekrarı uyuşmamakta"

    if (name == password):
        # != demişsin == olacak
        errors = "Parolanız adınız ve soyadınız ile aynı olamaz!"
    if(errors == None):
        # Eğer herhangi bir hata yoksa(şifre ve şifre tekrarı aynıysa, kullanıcı adı doluysa vs.) kayıt işlemine başlayabiliriz.

        # User modelimizde register() diye bir metot var ve o Nokta oluşturuyor fakat oluşturacağı kullanıcı adını modelin başlatıcısından alıyor. Hani construct diye bir şey vardı ya Java'da işte o.
        user = User(username) # Kullanıcıdan gelen (formdan) kullanıcı adıyla User'ı başlatıyoruz. == User("seymasa") gibi
        # bunları register'a vermen lazım başlatıcıya değil. Yoksa her kullanıcıyla işlem yapman gerektiğinde ad soyad vs göndermen gerekecek

        # Artık user modelimize nesne oluşturduğumuza göre .register() metotunu kullanabiliriz.
        user.register(password, name, email,) # ilk parametre olarak oluşturulacak User noktasının olacağı şifreyi istiyor. Bu şifreyi de kullanıcıdan aldığımız şifreyle yapacağız.
        # bu kadar bitti
        return redirect(url_for('login'))
    else:
        return render_template("register.html", errors=errors)



@app.route('/post', methods=['POST'])
def post():
  text = request.form['turpMesaj']
  if not text:
      flash('Bisiler yazmadan gönderemezsin')
  else:
      post = User(session['username']).post(text)
      print(post)
      return render_template('post.html', username=session.get('username'), post=post)


@app.route('/like', methods=['POST'])
def like():
    postId = request.form['postId']
    username = session.get('username')
    User(username).like(postId, username)
    return "1"



@app.route('/login', methods= ['GET'])
def login():
    return render_template('login.html')



@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')



""" @app.route("/logout")
@login_required
def logout():
    session.pop('username', None)
    flash('Logged out.')
    return redirect(url_for('login'))  """






@app.route('/', methods= ['GET'])
def homepage():
    if not session.get('username'):
        return redirect(url_for('login'))
    else:
        return render_template("index.html")



@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('static/assets', path)

#####################################################################################

@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    """
    posts = get_users_recent_posts(username)
    similar= []
    common = []
    viewer_username = session.get('username')
    if viewer_username:
        viewer= User(viewer_username)
        if viewer.username == username:
            similar = viewer.get_similar_users()
        else:
        common = viewer.get_commanality_of_user(username)
    return render_template(
        'profile.html',
        username= username,
        posts= posts,
        similar= similar,
        common= common
        )
    """
    pass

@app.route('/account-settings', methods=['GET'])
def accountSettings():
    pass

@app.route('/update-account', methods=['POST'])
def updateAccount():
    pass

@app.route('/<kullaniciAdi>/follow', methods=['GET'])
def follow(kullaniciAdi):
    pass

@app.route('/call', methods=['POST'])
def call():
    pass