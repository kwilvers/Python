# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import math

@st.cache_data
def load_data():
    df = pd.read_csv("./bullesverre.csv", sep=";")
    df = df[["lat", "lon", "ville", "cp", "poidsmax"]]
    # Pour le Pydeck aucune valeur ne peut être null
    #df = df.query('poidsmax'.notnull())
    villes = df['ville'].unique()
    poidsmax = df['poidsmax'].unique()
    return (df, villes, poidsmax)

def get_color(poidsmax):
    if math.isnan(poidsmax):
        return 'red'
    elif poidsmax <= 900:
        return 'orange'
    else:
        return 'green'

def get_icon(poidsmax):
    if math.isnan(poidsmax):
        kw = {"prefix": "fa", "color": "red", "icon": "bottle-water"}
        return folium.Icon(**kw)
    elif poidsmax <= 900:
        kw = {"prefix": "fa", "color": "orange", "icon": "bottle-water"}
        return folium.Icon(**kw)
    else:
        kw = {"prefix": "fa", "color": "green", "icon": "bottle-water"}
        return folium.Icon(**kw)


df, villes, poidsmax = load_data()

st.title("Carte des bulles à verre")
st.subheader("Visualisation des bulles à l'aide de Folium")

st.sidebar.header("Paramètres")
# Filtre par commune
option = st.sidebar.selectbox('Selectioner une ville :', villes)
df = df.query(f"ville == '{option}'")

poidsmax = df['poidsmax'].unique()
poidsmaxselected = st.sidebar.selectbox('Poids max :', poidsmax)
if math.isnan(poidsmaxselected):
    df = df.query(f"poidsmax.isna()", engine='python')
else:
    df = df.query(f"poidsmax <= {poidsmaxselected} or poidsmax.isna()")

with st.expander("Data Table"):
    st.dataframe(df)

# Map 2d
st.title("Carte Folium", anchor="center")

maptiles = st.sidebar.radio(
    "Map tiles",
    ["OpenStreetMap", "Cartodb Positron", "Cartodb dark_matter"],
    key="visibility",
)

m = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=10, tiles=maptiles)
kw = {"prefix": "fa", "color": "green", "icon": "arrow-up"}
icon = folium.Icon(angle=180, **kw)
radius = 5

for idx, row in df.iterrows():
    folium.Marker([row['lat'], row['lon']], 
                  icon=get_icon(row["poidsmax"]), 
                  tooltip=str(row["poidsmax"])).add_to(m)

# Affichage de la carte dans Streamlit
folium_static(m)

st.header("Find icon on : https://fontawesome.com/search")