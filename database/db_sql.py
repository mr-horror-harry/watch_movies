import sqlite3, datetime
from database.queries import CREATE_MOVIES, INSERT_MOVIE, SELECT_MOVIE, SELECT_BY_DATE, DELETE_MOVIE
from database.queries import CREATE_WATCHLIST, INSERT_WATCHED, SELECT_WATCHED

connection = sqlite3.connect("./database/movies_data.db")
connection.row_factory = sqlite3.Row

def createTable() -> None:
    with connection:
        connection.execute(CREATE_MOVIES)
        connection.execute(CREATE_WATCHLIST)

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

def moveMovies(user_name, movie_name):
    with connection:
        connection.execute(DELETE_MOVIE, (movie_name,))
        connection.execute(INSERT_WATCHED, (user_name, movie_name))

def getWatched(user_name):
    with connection:
        cursor = connection.execute(SELECT_WATCHED, (user_name, ))
        return cursor

def delMovie(movie_name):
    with connection:
        cursor = connection.execute(DELETE_MOVIE, (movie_name,))