import folium
import pandas

df1 = pandas.read_csv('files/Volcanoes.txt')
df2 = df1.iloc[:, 8:10]  # list(df1["LAT"])
df3 = list(df1["NAME"])
elev = list(df1["ELEV"])

map = folium.Map(location=[df2.LAT[61], df2.LON[61]])
fg1 = folium.FeatureGroup(name="My Map")


def getColor(el):
    c = 'green'
    if(int(el) >= 2000):
        c = 'orange'
    if(int(el) >= 3000):
        c = 'red'
    return c


for i, na, el in zip(range(0, len(df1)), df3, elev):
    c = getColor(el)
    fg1.add_child(folium.CircleMarker(location=[df2.LAT[i], df2.LON[i]], popup=str(na), radius=7, color=c, fill=True,
                                      fill_color=c))

fg2 = folium.FeatureGroup(name="My Map")
fg2.add_child(folium.GeoJson(data=(open('files/world.json', 'r',
                                        encoding='utf-8-sig').read()), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 20000000
                                                                                                 else 'orange' if 20000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))

fg1.layer_name = 'Volcaones'
fg2.layer_name = 'Population'
map.add_child(fg1)
map.add_child(fg2)
folium.LayerControl().add_to(map)
map.save("Map1.html")
