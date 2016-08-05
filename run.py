import os
from social import app

app.secret_key = os.urandom(24) #uygulama şifreleme (rastgele 24 karakterlik)
app.run(debug=True, port=1453) #uygulama balatıcı
