import sqlite3, datetime
from database.queries import CREATE_MOVIES, INSERT_MOVIE, SELECT_MOVIE, SELECT_WATCHED, SELECT_BY_DATE, SET_WATCHED

connection = sqlite3.connect("./database/movies_data.db")
connection.row_factory = sqlite3.Row

def createTable() -> None:
    with connection:
        connection.execute(CREATE_MOVIES)

#add a new movie
def addMovie(name, release_date):
    with connection:
        connection.execute(INSERT_MOVIE, (name, release_date))

def getMovies(upcoming=False):
    #movies to be released
    if upcoming:
        today = str(datetime.datetime.today()).split(" ")[0]
        with connection:
            cursor=connection.execute(SELECT_BY_DATE, (today, ))
            return cursor
    #all movies list
    else:
        with connection:    
            cursor=connection.execute(SELECT_MOVIE)
            return cursor

def watchMovies(movie_name):
    with connection:
        connection.execute(SET_WATCHED, (movie_name, ))

def getWatched():
    with connection:
        cursor = connection.execute(SELECT_WATCHED)
        return cursor

def delMovie():
    with connection:
        cursor = connection.execute(DELETE_MOVIE, (movie_name,))