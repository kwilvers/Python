import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.features import DivIcon
import pandas as pd

d = {
    'id': [1, 2, 3, 4, 3, 4, 5], 
    'Country': ['Belgium', 'France', 'Spain', 'Italy', 'Germany', 'Finland', 'Greece'],
    'Data': [12, 244, 31, 44, 355, 44, 578] 
    }
df = pd.DataFrame(data=d)

dfC = pd.read_csv("./country-centroids.csv")
df = df.merge(dfC, how='inner', left_on="Country", right_on="name")

with st.expander("Df"):
    st.dataframe(df)

#Setting up the world countries data URL
country_shapes = f'./country-border.json'
m = folium.Map(tiles="Cartodb Positron")

if st.checkbox("Show colors"):
    folium.Choropleth(
        geo_data=country_shapes,
        name='My test',
        data=df,
        columns=['Country', 'Data'],
        key_on='feature.properties.name',
        fill_color='PuRd',
        nan_fill_color='white',
        legend_name="Country test",
        highlight=True
    ).add_to(m)

for idx, row in df.iterrows():
    if( not pd.isnull(row['latitude']) and not pd.isnull(row['longitude'])):
        folium.map.Marker(
                [row['latitude'], row['longitude']], 
                tooltip=str(row["Country"]),
                icon=DivIcon(
                icon_size=(250,20),
                icon_anchor=(0,0),
                html='<div style="font-size: 10pt; font-weight:bold;">'+f"{row['Data']}"+'</div>',
                )
            ).add_to(m)

folium_static(m)