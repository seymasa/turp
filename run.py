import os
from social import app
app.config['NEO4J_USERNAME'] = "neo4j"
app.config['NEO4J_PASSWORD'] = "şifren"

app.secret_key = os.urandom(24) #uygulama şifreleme (rastgele 24 karakterlik)
app.run(debug=True) #uygulama balatıcı
