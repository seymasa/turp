from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
import os
import uuid

url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474') # Ortam değişkenlerinden çek
username = os.environ.get('NEO4J_USERNAME', 'neo4j') # ortam değişkenlerinden çek bulamazsan 2. parametreyi kullan
password = os.environ.get('NEO4J_PASSWORD', 'ss1510')

graph = Graph(url, username=username, password=password)
class User:
    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.find_one("User", "username", self.username) # User etiketli noktalardan, username sütunu self.username 'e eşit olanı getir (find_one) = (bir tane getir)
        return user

    def register(self, password):
        if not self.find(): # Eğer bu kullanıcı adından kimse yoksa, kayıt yap
            user = Node('User', username=self.username, password=bcrypt.encrypt(password))
            graph.create(user)
            return True
        else:
            return False

    def post(self, user, content):  # Post.add çağırılırken kullanıcı ve içerik belirtilsin
        user = self.find()
        post = Node(
            "Post",
            id=str(uuid.uuid4()),
            text=content
        )  # post noktası oluşturulsun
        rel = Relationship(user, "POSTED_BY", post)  # oluşturulan post ile fonksiyon çağırılırken ki user bağlansın
        graph.create(rel)  # bu bağlantıyı oluştur.

    """def timestamp():
        epoch = datetime.utcfromtimestamp(0)
        now = datetime.now()
        delta = now - epoch
        return delta.total_seconds()  """

    def date():
        return datetime.now().strftime('%Y-%m-%d')

    def login_check(self, password):
        if (Node('User', username=self.username, password=bcrypt.encrypt(password))):
            return True
        else:
            return False


class Post:
    def __init__(self):
        pass

    def like(self, user, post_id):
        post= graph.find_one("Post", "id", post_id)
        graph.create_unique(Relationship(user, "LIKED", post))
