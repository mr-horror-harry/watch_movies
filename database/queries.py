#queries list
#
CREATE_MOVIES = """
CREATE TABLE IF NOT EXISTS movies (
    movie_name TEXT,
    release_date DATE,
    status INTEGER
);
"""
INSERT_MOVIE = "INSERT INTO movies (movie_name, release_date, status) VALUES (?,?,0);"
SELECT_MOVIE = "SELECT * FROM movies;"
SELECT_BY_DATE = "SELECT * FROM movies WHERE release_date>?;"
DELETE_MOVIE = "DELETE FROM movies WHERE movie_name=?"

#movie list for the watched menu
CREATE_WATCHLIST="""
CREATE TABLE IF NOT EXISTS watchlist(
    user_name TEXT,
    movie_name TEXT
);
"""
INSERT_WATCHED = "INSERT INTO watchlist (user_name, movie_name) VALUES (?, ?);"
SELECT_WATCHED = "SELECT * FROM watchlist WHERE user_name=?;"