#queries list
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
SELECT_WATCHED = "SELECT * FROM movies WHERE status=1;"
SET_WATCHED = "UPDATE movies SET status=1 WHERE movie_name=?;"
DELETE_MOVIE = "DELETE FROM movie WHERE movie_name=?"
