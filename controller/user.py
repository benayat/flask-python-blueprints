from flask import Response, make_response, Blueprint, request,jsonify
import json

from flask_jwt_extended import jwt_required,get_jwt_identity
from datetime import timedelta

from database.models import User
from mongoengine.errors import DoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from .errors import SchemaValidationError, EmailAlreadyExistsError, InternalServerError, \
UpdateUserError, UserDoesNotExistsError,UnauthorizedError


  

users = Blueprint('users', __name__)

@users.route('/users',methods=["GET"])
def get_users():
    print("getting all users")
    users=User.objects().to_json()
    return Response(users,mimetype="application/json", status=200)
    
# I prefer to use the Response class, but since it can't return many types as data, 
# I'll just serialize the dictionary to a json string with json.dumps.

@users.route("/users", methods=["POST"])
def sign_up():
    try:
        body=request.get_json()
        body["password"]=User.encryptPassword(body)
        print(body["password"])
        user=User(**body).save(force_insert=True)
        id=user.id
        print(str(id))
        return Response(json.dumps({'id':str(id)}),mimetype="application/json",status=201)
    except NotUniqueError:
        raise EmailAlreadyExistsError
    except Exception as e:
        raise InternalServerError

@users.route("/users/login", methods=["POST"])
def login():
    try:
        body=request.get_json()
        print(body)
        user = User.objects.get(email=body.get('email'))
        print(user)
        print(type(body["password"]))
        if user.check_password(body["password"]):
            print("pasword is ok!")
            user.generateAuthToken().save()
            print(user.token)
            return  {'token': user.token}, 200
        else:
            raise UnauthorizedError
    except UnauthorizedError:
        raise UnauthorizedError
    except Exception:
        raise InternalServerError

@users.route("/users/<string:email>",methods=["PUT"])
@jwt_required()
def update_password(email):
    try:
        body=request.get_json()
        User.objects.get(email=email).update(**body)
        return 'updated successfuly', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdateUserError
    except Exception:
        raise InternalServerError 
    
@users.route('/users/<string:id>',methods=["DELETE"])
@jwt_required()
def delete_user(id):
    try:
        User.objects.get(id=id).delete()
        return '',200
    except DoesNotExist:
        raise UserDoesNotExistsError
    except Exception:
        raise InternalServerError

""" 
thoughts:
- update - only password should be updateable?
- accessing - do I even need the Id if the email is unique? or just use the email?

 """