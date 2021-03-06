from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from time import gmtime, strftime
from pytz import timezone
import datetime
import os
import random


url = 'http://localhost:7474'
username = 'neo4j'
password = 'seymasa'

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
        turkey = timezone('Europe/Istanbul')
        post = Node(
            "Post",
            number=random.randint(10000000000, 99999999999),
            text=content,
            username=self.username,
            postTime=turkey.localize(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        )  # post noktası oluşturulsun
        rel = Relationship(post, "POSTED_BY", user)  # oluşturulan post ile fonksiyon çağırılırken ki user bağlansın
        graph.create(rel)  # bu bağlantıyı oluştur.
        return post

    def follow(self, other):
        user = self.find()
        print(other)
        othernode = graph.find_one("User", "username", other)
        print(othernode)
        print(user)
        rel = Relationship(user, "FOLLOW", othernode)
        return graph.create(rel)

    def PostList(self):
        postQuery = "Match (cur_user: User {username: '"+self.username+"'})-[:FOLLOW]->(others: User)<- [:POSTED_BY]-(p: Post) with cur_user, p, others Match(l: Post)-[:POSTED_BY]->(cur_user) Return collect(distinct p) + collect(distinct l) as posts"
        print(postQuery)
        result = graph.run(postQuery).data()
        return result

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

    """
    def timeline_following(self, user_id):
        query_string =
                start cur_user=node(%d)
                match cur_user - [:FOLLOW]->(user) - [:POSTED_BY]->(post)
                return
                count(r) as cnt_like,
                post.text as text,
                ID(post) as post_id,
                ID(user) as user_id,
                user.username as username,
                user.email as email,
                post.date as date
                order by post.date desc;
            % (user_id)


    result = neo4j.CypherQuery(graph_db, query_string).execute()

    return result
"""

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