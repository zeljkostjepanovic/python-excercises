import folium
import pandas as pd

map = folium.Map(location=[48.7767982,-121.8109970], zoom_start=4, tiles = "Stamen Terrain")

fg1 = folium.FeatureGroup(name="Volcanoes in US")
fg2 = folium.FeatureGroup(name="Population")

volcanoes = pd.read_csv('Volcanoes.txt')
lon = list(volcanoes["LON"])
lat = list(volcanoes["LAT"])
elev = list(volcanoes["ELEV"])
vname = list(volcanoes["NAME"])

popup_content = """
<a href="https://duckduckgo.com/?q={} volcano">{} Volcano</a><br>
Elevation: {}m
"""

def elevation_color(elv):
    if elv < 1000:
        col = "green"
    elif elv in range(1001,1999):
        col = "blue"
    elif elv in range(2000,2999):
        col = "orange"
    else:
        col = "red"
    return col

for lt, ln, elv, nm in zip(lat,lon,elev,vname):
    fg1.add_child(folium.Marker(location=[lt,ln], icon=folium.Icon(color=elevation_color(elv), prefix='fa', icon='camera-retro'), 
    radius=150, popup=popup_content.format(nm,nm,elv),))

fg2.add_child(folium.GeoJson(data=(open("world.json",'r', encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000 
else 'blue' if  20000000 <= x['properties']['POP2005'] < 200000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map1.html")