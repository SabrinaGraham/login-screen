from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__='userdata'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True)
    password=db.Column(db.String(255))
    created=db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, password):
        self.username=username
        self.password=generate_password_hash(password, method='pbkdf2:sha256')
