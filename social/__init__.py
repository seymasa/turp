from .views import app
"""from .models import graph

def unique_alan(etiket,sutun): #unique_alan('user', 'username')
    sorgu= "CREATE CONSTRAINT ON (n:{label}) ASSERT n.{property} IS UNIQUE" # Etiketteki noktaların şu sütunu benzersiz olmalıdır.
    sorgu= sorgu.format(label=etiket, property=sutun) #sorgu string'ini ayarlıyoruz şuan
    graph.cypher.execute(sorgu) # execute (exe) çalıştır......

unique_alan("User", "username")
unique_alan("User", "email")"""