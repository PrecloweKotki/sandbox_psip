import folium
from bs4 import BeautifulSoup
import requests
import re

# Pobranie strony

town_name = input("STATE THE NAME OF TOWN TO SEARCH")

def get_coordinates(city:str)->list[float,float]:
 URL_adress = (f'https://pl.wikipedia.org/wiki/{city}')
 response = requests.get(url=URL_adress)
 response_html = BeautifulSoup(response.text, 'html.parser')
# Pobranie współrzędnych
 response_html_latitude = response_html.select('.latitude')[1].text
 response_html_latitude = float(response_html_latitude.replace(',','.'))
 response_html_longitude = response_html.select('.longitude')[1].text
 response_html_longitude = float(response_html_longitude.replace(',','.'))
 return [response_html_latitude,response_html_longitude]
print(get_coordinates(town_name))

###Rysowanie mapy
town = get_coordinates(town_name)
map = folium.Map(location = town,tiles= "OpenStreetMap",zoom_start=11)
folium.Marker(
 location= town,
 popup=[town_name,"GEOINFORMATYKA"],
 icon= folium.Icon(color="purple")
).add_to(map)
map.save('mapa.html')