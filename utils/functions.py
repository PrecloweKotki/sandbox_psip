import folium
import psycopg2 as ps
from bs4 import BeautifulSoup
import requests


#GUI
def gui() -> None:
    while True:
        print(f'MENU: \n'
              f'ADD \n'
              f'REMOVE \n'
              f'BROWSE \n'
              f'UPDATE \n'
              f'MAP SELECT \n'
              f'MAP ALL \n'
              f'EXIT \n')
        odp = input(f'PICK A FUNCTION')
    #What happens after you pick an option
        match odp:
            case " ADD":
                name = input("Enter name: ")
                nickname = input("Enter nick: ")
                town = input("Enter city: ")
                posts = input("Enter posts: ")
                ADD_USER(name, nickname, town, posts)
            case " REMOVE":
                nickname_to_remove = input("Enter nickname of user to remove: ")
                REMOVE_USER(nickname_to_remove)
            case " BROWSE":
                BROWSE_USER()
            case " UPDATE":
                update_nickname = input("Enter the nickname to update: ")
                new_name = input("Enter new name: ")
                new_nickname = input("Enter new nickname: ")
                new_town = input("Enter new town: ")
                new_posts = input("Enter new number of posts: ")
                UPDATE_USER(update_nickname, new_name, new_nickname, new_town, new_posts)
            case " MAP SELECT":
                nickname = input("Pick the nickname you would like to see on the map: ")
                CREATE_MAP_SELECT(nickname)
            case " MAP ALL":
                CREATE_MAP_ALL()
            case " EXIT":
                print('MAPBOOK EXITED SUCCESSFULLY!')
                break



#Connection to PostGreSQL server
db_params = ps.connect(
    database='postgres',
    user="postgres",
    password="Koczodan",
    host="localhost",
    port=5432
)

cursor = db_params.cursor()

#Adding an user
def ADD_USER(name, nickname, town, posts):
    sql_query = f"INSERT INTO public.users(name, nickname,town, posts) VALUES (%s,%s, %s,%s);" #The program will insert the values
    data = (name, nickname, town, posts) #What the program will insert
    cursor.execute(sql_query, data) #Doing it
    db_params.commit() #Commiting it to the server

#Removing an user based on the nickname
def REMOVE_USER(nickname_to_remove):
    sql_query = f"DELETE FROM public.users WHERE nickname = %s;" #Remove an user whose nickname I picked
    data = (nickname_to_remove,) #What the program will search for
    cursor.execute(sql_query, data) #Removing the nickname I searched
    db_params.commit() #Commiting it to the server

    #Modifying an user
def UPDATE_USER(nickname_to_update, new_name, new_nickname, new_town, new_posts):
    sql_query = f"UPDATE public.users SET name=%s, nickname=%s, town=%s, posts=%s WHERE nickname=%s;" #Code to update the whole entry based on searched nickname
    data = (new_name, new_nickname, new_town, new_posts, nickname_to_update) #What the program will modify and search for
    cursor.execute(sql_query, data) #Modifying
    db_params.commit() #Commiting it to the server

#Showing all entries
def BROWSE_USER():
    sql_query = f"SELECT * FROM public.users ;" #It will show all users
    cursor.execute(sql_query)
    db_params.commit()
    rows = cursor.fetchall()#Returns with the entries
    for row in rows:
        print(row) #Prints them so that I could see them

#Creating a map for one user

def get_coordinates_of(town: str) -> list[float]:
        adres_URL = f'https://pl.wikipedia.org/wiki/{town}'
        response = requests.get(url=adres_URL)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude_elements = response_html.select('.latitude')
        longitude_elements = response_html.select('.longitude')
        if len(latitude_elements) > 1 and len(longitude_elements) > 1:
            response_html_latitude = float(latitude_elements[1].text.replace(',', '.'))
            response_html_longitude = float(longitude_elements[1].text.replace(',', '.'))
            return [response_html_latitude, response_html_longitude]
        else:
            print(f"Coordinates not found for {town}.")
            return None
def CREATE_MAP_SELECT(nickname: str) -> None:
    cursor.execute(f"SELECT * FROM users WHERE nickname = %s", (nickname,))
    user = cursor.fetchone()
    if user:
        city = user[2]
        city_coordinates = get_coordinates_of(city)
        map = folium.Map(
            location=city_coordinates,
            tiles="OpenStreetMap",
            zoom_start=14,
        )
        folium.Marker(
            location=city_coordinates,
            popup=f'USER: {user[0]}, POSTS: {user[3]}'
        ).add_to(map)
        map.save(f'MAP_{user[1]}.html')
    else:
        print(f"User called {nickname} not found in the database.")


    #Drawing a map for all users
def CREATE_MAP_ALL() -> None:
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()

    if all_users:
        map = folium.Map(
            location=[52.3, 21.0],
            tiles="OpenStreetMap",
            zoom_start=14,
        )

        for user in all_users:
            city_coordinates = get_coordinates_of(user[2])
            folium.Marker(
                location=city_coordinates,
                popup=f'USER: {user[0]} \nPOSTS: {user[3]}'
            ).add_to(map)

        map.save('MAP_ALL.html')
    else:
        print("No users found in the database.")
