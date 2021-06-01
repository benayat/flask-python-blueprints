class Error(Exception):
    # def __init__(self, type, status):
    #     self.message = errors[type]
    #     self.status=status
    pass
    # base error class
class InternalServerError(Error):
    pass

class SchemaValidationError(Error):
    pass

class MovieAlreadyExistsError(Error):
    pass

class UpdatingMovieError(Error):
    pass

class DeletingMovieError(Error):
    pass

class MovieDoesNotExistsError(Error):
    pass

class EmailAlreadyExistsError(Error):
    pass

class UnauthorizedError(Error):
    pass

class EmailDoesnotExistsError(Error):
    pass

class BadTokenError(Error):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "MovieAlreadyExistsError": {
         "message": "Movie with given name already exists",
         "status": 400
     },
     "UpdatingMovieError": {
         "message": "Updating movie added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting movie added by other is forbidden",
         "status": 403
     },
     "MovieDoesNotExistsError": {
         "message": "Movie with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
     "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
     }
}
