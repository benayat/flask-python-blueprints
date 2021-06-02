from enum import unique
from .db import db
import bcrypt
from flask_jwt_extended import create_access_token
from datetime import  timedelta

        
class User(db.Document):
    email = db.EmailField(required=True, max_length=40, unique=True)
    password = db.StringField(required=True)
    token = db.StringField(default=None)
    
    def encryptPassword(userRaw):
        salt = bcrypt.gensalt(rounds=8)
        encoded = userRaw["password"].encode('utf-8')
        password = bcrypt.hashpw(encoded, salt)
        return password
  
    def check_password(self , rawPassword):
        return bcrypt.checkpw(rawPassword.encode('utf-8'), self.password.encode('utf-8'))
    def generateAuthToken(self):
        expires = timedelta(days=7)  
        self.token = create_access_token(identity=str(self.id), expires_delta=expires)

""" 
thoughts: 
- do I even need a name? or maybe not? 
- what other fields does user have? list of movies? anything else? 

 """