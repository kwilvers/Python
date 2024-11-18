# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import time
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

df, villes, poidsmax = load_data()

st.sidebar.header("Paramètres")
# Filtre par commune
option = st.sidebar.selectbox('Selectioner une ville :', villes)
df = df.query(f"ville == '{option}'")

poidsmax = df['poidsmax'].unique()
poidsmaxselected = st.sidebar.selectbox('Poids max :', poidsmax)
if math.isnan(poidsmaxselected):
    df = df.query(f"poidsmax.isna()", engine='python')
else:
    df = df.query(f"poidsmax <= {poidsmaxselected}")
st.dataframe(df)

if not st.sidebar.checkbox('Essayer pydeck'):
    # Map 2d
    st.title("Carte 2d", anchor="center")
    st.map(df)
else:
    if len(df.index) == 0:
        st.warning("No data to plot")
    else:
        # Map 3d pydeck
        st.title("Carte 3d pydeck", anchor="center")
        place_holder = st.info("Updating map")
        time.sleep(1)
   
    
        view_state=pdk.ViewState(
                latitude=df.iloc[0]["lat"],
                longitude=df.iloc[0]["lon"],
                zoom=13.5,
                pitch=50)
        
        hexagon_layers=pdk.Layer(
                    'HexagonLayer',
                    data=df,
                    get_position=["lon", "lat"],
                    opacity=0.5,
                    radius=35,
                    filled=True,
                    extruded=True,
                    elevation_scale=2,
                    get_elevation="poidsmax",
                    pickable=True )
        
        place_holder.pydeck_chart(pdk.Deck(
             map_style='mapbox://styles/mapbox/light-v9',
             initial_view_state=view_state,
             layers=[hexagon_layers],
             tooltip={"html": "<b>Poids max.: </b> {elevationValue}", "style": {"color": "white"}}
         ))