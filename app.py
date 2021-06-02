
import os
from werkzeug.exceptions import HTTPException

from flask import Flask
from database.db import initialize_db
from flask_jwt_extended import JWTManager
from controller.user import users
# if I compare it to express, it's just like importing a router into the app.js file.
app=Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
jwt = JWTManager(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'moviesDB',
    'host': "mongodb+srv://benayat:fmWAK3TLrJwHxr8@cluster0.ptwdq.mongodb.net/moviesDB?retryWrites=true&w=majority",
}
initialize_db(app)

app.register_blueprint(users)

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e


app.run()
# app.run(debug=True)


# to sum it up: all the blueprint does is just to import sub-routers into the app.
