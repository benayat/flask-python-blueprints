#~movie-bag/database/db.py
from flask_mongoengine import MongoEngine
db=MongoEngine()
def initialize_db(app):
    print("initializing db")
    db.init_app(app)
    