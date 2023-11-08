from database.db_sql import createTable, addMovie, getMovies, moveMovies, getWatched, delMovie
import datetime
choice="""
-------User Menu-------
1) Add a movie
2) View new releases
3) View all movies
4) Watch a Movie
5) View watched Movies
6) Delete a Movie
e) exit

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

def printDataWtached(title, user_name, movies_list):
    print(f"\n-------{title}-------\n{user_name}:")
    for user_data in movies_list:
        print(user_data["movie_name"])

def promptWatch():
    user_name = input("Enter the user name: ")
    movie_name = input("Enter the movie name you watched: ")
    moveMovies(user_name, movie_name)
    print("Movies moved Successfully!")

def promptWatchedOver():
    user_name = input("Enter the user name: ")
    data_watched = getWatched(user_name)
    printDataWtached("Watched Movies", user_name, data_watched)

def delPrompt():
    movie_name = input("Enter the movie name you watched: ")
    delMovie(movie_name)
    print("Movie Deleted!")

while((ip:=input(choice)) != "e"):
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
        promptWatchedOver()

    elif ip=="6":
        delPrompt()

    else:
        print("Invalid user input!")