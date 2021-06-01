
from flask import Response, Blueprint, request
# from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from database.models import Movie
from mongoengine.errors import FieldDoesNotExist, DoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from .errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, \
UpdatingMovieError, DeletingMovieError, MovieDoesNotExistsError

movies = Blueprint('movies', __name__)
# @movies.route("/")
# def hello_world():
#     return "hellow world"
@movies.route('/movies',methods=["GET"])
def get_movies():
    print("getting all movies")
    movies=Movie.objects().to_json()
    return Response(movies,mimetype="application/json", status=200)
    
# I prefer to use the Response class, but since it can't return many types as data, 
# I'll just serialize the dictionary to a json string with json.dumps.
@movies.route("/movies", methods=["POST"])
def add_movie():
    try:
        body=request.get_json()
        movie=Movie(**body).save(force_insert=True)

        id=movie.id
        print(str(id))
        return Response(json.dumps({'id':str(id)}),mimetype="application/json",status=201)
    except NotUniqueError:
        raise MovieAlreadyExistsError
    except Exception as e:
        raise InternalServerError

@movies.route("/movies/<string:id>",methods=["PUT"])
def update_movie(id):
    try:
        body=request.get_json()
        Movie.objects.get(id=id).update(**body)
        return 'updated successfuly', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingMovieError
    except Exception:
        raise InternalServerError 
    
@movies.route('/movies/<string:id>',methods=["DELETE"])
def delete_movie(id):
    try:
        Movie.objects.get(id=id).delete()
        return '',200
    except DoesNotExist:
        raise MovieDoesNotExistsError
    except Exception:
        raise InternalServerError
@movies.route('/movies/<string:id>',methods=["GET"])
def get_movie(id):
    try:
        movie=Movie.objects.get(id=id).to_json()
        # print(movie)
        return Response(movie,mimetype="application/json",status=200)
    except DoesNotExist:
        raise MovieDoesNotExistsError
