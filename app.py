from database.db_sql import createTable, addMovie, getMovies, watchMovies, getWatched, delMovie
import datetime
choice="""
-------User Menu-------
1) Add a movie
2) View new releases
3) View all movies
4) Watch a Movie
5) View watched Movies
6) Delete a Movie

Enter your choice: """

print("Welcome to the movie list app!")
createTable()

def userInput():
    movie_name = input("Movie Name: ")
    release_date = input("Release Date (YYYY-MM-DD): ")
    addMovie(movie_name, release_date)
    print("Data inserted!")

def printData(title, movies_list):
    print(f"\n-------{title}-------")
    for movie in movies_list:
        print(movie["movie_name"], movie["release_date"])

def promptWatch():
    movie_name = input("Enter the movie name you watched: ")
    watchMovies(movie_name)

def deletePrompt():
    movie_name = input("Enter the movie name you watched: ")
    delMovie(movie_name)

while((ip:=input(choice)) != "6"):
    if ip=="1":
        userInput()

    elif ip=="2":
        data_by_date =  getMovies(True)
        printData("New Releases", data_by_date)

    elif ip=="3":
        data_all = getMovies()
        printData("All Movies", data_all)

    elif ip=="4":
        promptWatch()

    elif ip=="5":
        data_watched = getWatched()
        printData("Watced Movies", data_watched)

    elif ip=="6":
        deletePrompt()

    else:
        print("Invalid user input! Quiting!")