# imports
from display import print_menu, print_header, clear
from album import Album
from song import Song
import pickle


# globals
# declare a catalog variable (list)
catalog = []
album_count = 0


# functions

def serialize_data():
    try:
        writer = open('sonMngr.data', 'wb')  # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")
    except:
        print("** Error, data not saved")


def deserialize_data():
    global album_count

    try:
        reader = open('songMngr.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)

        # get the last used id, and increase by 1
        last = catalog[-1]
        album_count = last.id + 1

        how_many = len(catalog)
        print('** Read: ' + str(how_many) + " albums")

    except:
        print("** Error, no data file found")


def register_album():
    global album_count
    print_header("Register new Album")

    try:
        # title, genre, artist, release_year, price, album_art, related_artist, record_label
        title = input("Please provide Title: ")
        genre = input("Please provide Genre: ")
        artist = input("Please provide Artist Name: ")
        release_year = int(input("Please provide Release year: "))
        price = float(input("Please provide price: "))
        album_art = input("Please provide Album_Art URL: ")
        related_artist = input("Please provide Related Artist: ")
        record_label = input("Please provide Record Label: ")

        album_count += 1

        album = Album(album_count, title, genre, artist, release_year,
                      price, album_art, related_artist, record_label)

        # push the album into the list
        catalog.append(album)
        print("***Album Created!")

    except ValueError:
        print("***Error : invalid number, try again!!")

    except:
        print("**Unexpected Error. try Again!")


def print_albums():
    print_header("Your current albums")

    for album in catalog:
        print(f"{album.id} | {album.title} | {album.release_year}")


def register_song():

    # let the user choose an album
    print_albums()
    album_id = int(input("Please choose the album Id: "))

    # find the album with that Id
    found = False
    for album in catalog:
        if(album.id == album_id):
            found = True
            the_album = album

    if(not found):
        print("** Error: Wrong Id. Try again.")
        return

    # create the song

    print_header("Register a new Song")
    title = input("Please provide a Title: ")
    featured_artist = input("Please provide a Title Featured Artist: ")
    length_of_song = input("Please provide the Length in seconds: ")
    written_by = input("Please provide the Song Author: ")

    song = Song(1, title, featured_artist, length_of_song, written_by)

    # push the song to the album list
    the_album.add_song(song)

    print("**Song Registered")


def display_album_song():
    found = False
    print_albums()

    album_id = int(input("Please choose an ID: "))

    for album in catalog:
        if(album.id == album_id):
            found = True

            # print album songs list
            for song in album.songs:
                print(song.title)
    if(not found):
        print("***Error: Invalid album ID")


def count_songs():
    print_header("Your total number of songs")

    total = 0
    for album in catalog:
        songs_catalog = len(album.songs)
        total += songs_catalog

    print(f"There are: {total} songs in the system")

def total_price():
    print_header("Total amount of spent on albums")

    total_price = 0
    for album in catalog:
        album_price = album.price
        total_price += album_price
    print(f"Total amount of spent on Albums")

def most_expensive():
     print_header("Your most expensive album")

     total = 0
     for price in catalog:
         price_catalog = len(album.price)
         price += albums_catalog

def change_album_title():
    display_albums_songs()
    
    try:
        album_id = int(input("Please enter new album Title: "))

        #find the album with that Id
        found = False

        for album in catalog:
            if(album.id == album_id):
                found = True
                the_album = album

        if(not found):
            print("***ERROR, Please try again.")
            return

        new_title = the_album.title
        new_title = input("Please provide new Title: ")
        print(f"Your new title is: {new_title}")
        serialize_data()
    except:
        print("***ERROR, please enter a valid title and try again.")


# instructions
deserialize_data()
input("Press Enter to continue...")

opc = ''
while(opc != 'q' and opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_album()
        serialize_data()

    elif(opc == '2'):
        register_song()
        serialize_data()

    elif (opc == '3'):
        print_albums()

    elif (opc == '4'):
        display_album_song()

    elif(opc == '5'):
        count_songs()
    
    elif(opc == '6'):
        total_price()

    elif (opc == '7'):
        most_expensive()

    elif (opc == '8'):
        change_album_title()
        

    input("Press Enter to contiue")

clear()
