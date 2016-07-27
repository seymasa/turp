#from .models import User, Post
from flask import Flask, request, session, redirect, url_for, render_template, flash, send_from_directory
from flask_login import LoginManager, UserMixin,login_required, login_user,logout_user
from .models import User, Post # User modelini import ettik

app = Flask(__name__)

@app.route('/login', methods= ['POST'])
def doLogin():
    if request.method == 'POST':
        username=request.form["username"]
        password = request.form["password"]

        if len(username) <5:
            error ='Kullanıcı adın 6 karakterden küçük olamaz!'
        elif len(password) <5:
            error = 'Parola 6 karakterden küçük olamaz!'
        else:
            session['username'] = username
            flash("LOGGEND IN.")
            print("Giriş Yapıldı", username)
            return redirect(url_for("homepage"))
        return render_template('login.html', error=error)
        print(error)

@app.route('/login', methods= ['GET'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    error= None
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def doRegister(): # Kayıt ol formu gönderince burası çağırılıyor
    errors       = None
    name_surname = request.form['name-surname']
    username     = request.form['username']
    email        = request.form['email']
    password     = request.form['password']
    confirm      = request.form['confirm']

    if(password != confirm):
        errors = "Parola ve parola tekrarı uyuşmamakta"

    if (name_surname != password):
        errors = "Parolanız adınız ve soyadınız ile aynı olamaz!"
    if(errors == None):
        # Eğer herhangi bir hata yoksa(şifre ve şifre tekrarı aynıysa, kullanıcı adı doluysa vs.) kayıt işlemine başlayabiliriz.

        # User modelimizde register() diye bir metot var ve o Nokta oluşturuyor fakat oluşturacağı kullanıcı adını modelin başlatıcısından alıyor. Hani construct diye bir şey vardı ya Java'da işte o.
        user = User(username) # Kullanıcıdan gelen (formdan) kullanıcı adıyla User'ı başlatıyoruz. == User("seymasa") gibi
        # bunları register'a vermen lazım başlatıcıya değil. Yoksa her kullanıcıyla işlem yapman gerektiğinde ad soyad vs göndermen gerekecek

        # Artık user modelimize nesne oluşturduğumuza göre .register() metotunu kullanabiliriz.
        user.register(password, name_surname, email ) # ilk parametre olarak oluşturulacak User noktasının olacağı şifreyi istiyor. Bu şifreyi de kullanıcıdan aldığımız şifreyle yapacağız.
        # bu kadar bitti
        print("KAYDINIZ TAMAMLANDI Syn.", username)
        return redirect(url_for('login'))
    else:
        return render_template("register.html", errors=errors)


@app.route("/logout")
@login_required
def logout():
    session.pop('username', None)
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/add-post', methods=['POST'])
def post():
    text = request.form('text')
    if not text:
        abort(141, 'You must be logged in to add a post.')
    User(session('username')).add_past(text)
    return redirect(url_for('layout'))

@app.route('/like_post/<post_id>')
def like_post(post_id):
    username =session.get('username')

    if not username:
        abort(141,'You must be logged in to like a post.')

    User(username).like_post(post_id)

    flash('Liked Post!')
    return redirect(request.referrer)


@app.route('/account-settings', methods=['GET'])
def accountSettings():
    pass

@app.route('/update-account', methods=['POST'])
def updateAccount():
    pass



    """"""

@app.route('/<postId>/like', methods=['GET'])
def like(postId):
    pass

@app.route('/<kullaniciAdi>/follow', methods=['GET'])
def follow(kullaniciAdi):
    pass

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

@app.route('/', methods= ['GET'])
def homepage():
    return render_template('index.html')

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('static/assets', path)