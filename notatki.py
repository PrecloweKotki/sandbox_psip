import folium
from bs4 import BeautifulSoup
import requests
from dane import USER_LIST


# Pobranie strony
def get_coordinates(town_name: str) -> list[float, float]:
    URL_adress = (f'https://pl.wikipedia.org/wiki/{town_name}')
    response = requests.get(url=URL_adress)
    response_html = BeautifulSoup(response.text, 'html.parser')
    # Pobranie współrzędnych
    response_html_latitude = response_html.select('.latitude')[1].text
    response_html_latitude = float(response_html_latitude.replace(',', '.'))
    response_html_longitude = response_html.select('.longitude')[1].text
    response_html_longitude = float(response_html_longitude.replace(',', '.'))
    return [response_html_latitude, response_html_longitude]

def get_map_of(user: str) -> None:
    map = folium.Map(location=[52.3, 21.0], tiles="OpenStreetMap", zoom_start=4)
    for user in USER_LIST:
        folium.Marker(
            location=get_coordinates(user["town_name"]),
            popup=f'"USER: {user["name"]}\n'
                  f'"POST NUMBER:{user["posts"]}\n',
            icon=folium.Icon(color="purple")
        ).add_to(map)
    map.save('mapak.html')
###Rysowanie mapy

get_map_of(USER_LIST)