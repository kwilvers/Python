# -*- coding: utf-8 -*-

#
# pip install geopy
#

import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import datetime

st.title("Obtenir les coordonnées géographiques des lieux d'accidents d'avion")
st.subheader("pip install geopy", anchor="Center")
st.subheader("Géolocalisation des accidents d'avion par le lieu")
bt = st.button("Générer les coordonnées géographiques", icon="🌍")
if(bt):
    from geopy.geocoders import Photon
    # Une colonne "Location" du fichier CSV contient les 
    # noms des lieux à géolocaliser pour obtenir les 
    # coordonnées géographiques
    file_path = 'Airplane_Crashes_and_Fatalities_Since_1908.csv'
    data = pd.read_csv(file_path)
    # Initialiser le géo localisateur
    geolocator = Photon(user_agent="app_name here")
    # creating a single-element container
    placeholder = st.empty()

    # fonction pour obtenir la géolocalisation d’un lieu
    def get_coordinates(location):
        try:
            with placeholder.container():
                geo = geolocator.geocode(location, timeout=5,exactly_one=True)

                if geo:
                    st.write(f"{location} : {geo.latitude} , {geo.longitude}")
                    return geo.latitude, geo.longitude
                st.write(f"Pas de coordonées pour {location}")
            return None, None
        except Exception as e:
            st.write(f"Erreur de localisation de {location}")
            return None, None

    savedData = data
    data = data.head(10)
    # Applique la fonction à la colonne Location pour obtenir les coordonnées
    data[['Latitude', 'Longitude']] = data['Location'].apply(lambda loc: pd.Series(get_coordinates(loc)))
    # Sauvegarde les données dans un nouveau fichier CSV
    data.to_csv("newtest1.csv")
    st.write("Géolocalisation terminée, fichier sauvegardé")


file_path = 'newtest.csv'
df = pd.read_csv(file_path)

maptiles = st.sidebar.radio(
    "Map tiles",
    ["OpenStreetMap", "Cartodb Positron", "Cartodb dark_matter"],
    key="visibility",
)

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
min, max = df["Date"].min().year, df["Date"].max().year
st.write(f"Jeux de données de {min} à {max}")
#dt_from = st.sidebar.selectbox("De", df['Date'], 0)
#dt_to = st.sidebar.selectbox("a", df['Date'], 0)
dt_from = st.sidebar.slider("De", min_value=min, max_value=max, value=1976)
dt_to = dt_from + 1
st.write(f"Voir de {dt_from} à {dt_to}")
df = df[(df['Date'] >= datetime.datetime(dt_from,1,1)) & (df['Date'] <= datetime.datetime(dt_to,1,1))]
# Affiche les données
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10, tiles=maptiles)
kw = {"prefix": "fa", "color": "green", "icon": "arrow-up"}
icon = folium.Icon(angle=180, **kw)
radius = 5

marker_cluster = MarkerCluster().add_to(m)
#for idx, row in filtered_data.iterrows():
#    folium.CircleMarker([row['latitude'], row['longitude']], color=get_color(row['shore_distance'])).add_to(marker_cluster)
 
for idx, row in df.iterrows():
    if( not pd.isnull(row['Latitude']) and not pd.isnull(row['Longitude'])):
        folium.Marker([row['Latitude'], row['Longitude']], 
                    tooltip=str(row["Location"])).add_to(marker_cluster)

sw = df[['Latitude', 'Longitude']].min().values.tolist()
ne = df[['Latitude', 'Longitude']].max().values.tolist()

m.fit_bounds([sw, ne])

# Affichage de la carte dans Streamlit
folium_static(m)