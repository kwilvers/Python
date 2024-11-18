# Importation des bibliothèques nécessaires
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv('pirate_attacks.csv')
    country_df = pd.read_csv('country_codes.csv')
    return df, country_df

df, country_df = load_data()

# Fonction pour attribuer une couleur en fonction de la distance à la côte
def get_color(distance):
    if distance < 10:
        return 'green'
    elif distance < 50:
        return 'orange'
    else:
        return 'red'

# Création de l'application
def main():
    # Titre de l'application
    st.title("Carte des attaques de pirates")
    st.subheader("Visualisation des attaques de pirates à travers le monde")
    st.subheader("Filtrer les données par pays et par navire")
    st.subheader("Utilisation de carte Folium et MarkerCluster")

    # Ajout des multiselectbox pour les filtres
    country_options = st.multiselect('Sélectionnez un ou plusieurs pays', country_df[['country','country_name']].values.tolist(), format_func=lambda x: x[1])
    vessel_option = st.selectbox('Sélectionnez un navire', df['vessel_name'].unique())

    # Filtrage des données
    filtered_data = df[df['nearest_country'].isin([x[0] for x in country_options]) | (df['vessel_name'] == vessel_option)]

    # Création de la carte Folium
    m = folium.Map(location=[filtered_data['latitude'].mean(), filtered_data['longitude'].mean()], zoom_start=6, tiles='CartoDB Positron')

    # Ajout des points sur la carte avec MarkerCluster
    marker_cluster = MarkerCluster().add_to(m)
    for idx, row in filtered_data.iterrows():
        folium.CircleMarker([row['latitude'], row['longitude']], color=get_color(row['shore_distance'])).add_to(marker_cluster)

    # Affichage de la carte dans Streamlit
    folium_static(m)

    # Affichage des données filtrées
    st.dataframe(filtered_data)

# Exécution de l'application
if __name__ == "__main__":
    main()
