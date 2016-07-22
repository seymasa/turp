import app
import os

app.secret_key = os.urandom(24) #uygulama şifreleme (rastgele 24 karakterlik)
app.run(debug=True) #uygulama balatıcı