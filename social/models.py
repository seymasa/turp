from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
import os
import random
import dotenv

dotenv.load("../../.env")

url = dotenv.get('NEO4J_HOST', 'http://localhost:7474') # Ortam değişkenlerinden çek
username = dotenv.get('NEO4J_USERNAME', 'neo4j') # ortam değişkenlerinden çek bulamazsan 2. parametreyi kullan
password = dotenv.get('NEO4J_PASSWORD', 'neo4j')

graph = Graph(url, username=username, password=password)
class User:
    def __init__(self, username):
        self.username = username


    



    def find(self):
        user = graph.find_one("User", "username", self.username) # User etiketli noktalardan, username sütunu self.username 'e eşit olanı getir (find_one) = (bir tane getir)
        return user




    def register(self, password, name_surname, email):
        # zaten modelde biz şifreliyormuşuz. yani metota 123456 gönderince o şifreleyip veritabanına kaydediyormuş. O yüzden tekrar şifrelemiycez haydaaa :D Aydınlıklar geliyor bana bana :D
        if not self.find(): # Eğer bu kullanıcı adından kimse yoksa, kayıt yap
            user = Node('User', username=self.username, password=bcrypt.encrypt(password), name=name_surname, email=email)
            graph.create(user)

            return True
        else:
            return False



    def post(self, content):  # Post.add çağırılırken kullanıcı ve içerik belirtilsin
        user = self.find()
        post = Node(
            "Post",
            number=random.randint(10000000000, 99999999999),
            text=content
        )  # post noktası oluşturulsun
        rel = Relationship(post, "POSTED_BY", user)  # oluşturulan post ile fonksiyon çağırılırken ki user bağlansın
        graph.create(rel)  # bu bağlantıyı oluştur.
        return post

    def like(self, postId):
        user = self.find()
        post = graph.find_one("Post", "number", postId)
        print(postId)
        print(post)

        rel = Relationship(user, "LIKE", post)
        graph.create(rel)
        print(rel)


    def liked(self,postId):
        user = self.find()
        post = graph.find_one("Post", "number", postId)
        rel = Relationship(user, "DELETE", post)
        graph.delete(rel)
        print(rel)


    def login_check(self, password):

        user = self.find()
        if user: # Önceden eklediğim verileri sildim çünkü parolalarda sıkıntı çıkartacaktı bu şekilde doğru olur..
            return bcrypt.verify(password, user['password'])
        else:
            return False




    def login_use(self, username):

        user = self.find()
        if user:
            return user['username']
        else:
            return False




class Post:
    def __init__(self):
        pass

    #def call(self):
     #   graph.cypher.execute("MATCH (p: POST))")