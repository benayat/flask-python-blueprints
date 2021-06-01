
import os

from flask import Flask
from mongoengine import connect
from database.db import initialize_db
# if I compare it to express, it's just like importing a router into the app.js file.
from controller.movie import movies
app=Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'moviesDB',
    'host': "mongodb+srv://benayat:fmWAK3TLrJwHxr8@cluster0.ptwdq.mongodb.net/moviesDB?retryWrites=true&w=majority",
}
initialize_db(app)
app.register_blueprint(movies)
app.run(debug=True)


# to sum it up: all the blueprint does is just to import sub-routers into the app.
