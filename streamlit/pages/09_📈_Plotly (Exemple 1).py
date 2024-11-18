import streamlit as st
import pandas as pd
import plotly.express as px


# Fonction de chargement des données en cache 
# Les données sont chargée une fois
@st.cache_data
def load_data():
    df = pd.read_csv(R".\data.csv")
    # Différentes manière de trier les éléments
    df_be = df.query('ReportingCountry == "BE"')
    # Théorie des ensembles
    tg = ["Age<18","Age18_24","Age25_49","Age50_59","Age60_69","Age70_79","Age80+", "AgeUNK"]
    df_be_age = df_be[df.TargetGroup.isin(tg)]
    # Groupement par type de vaccin et sommation des doses
    d = df_be_age.groupby(by = "Vaccine")[["FirstDose", "SecondDose"]].sum()
    return d

# Chargement des données en cache
d = load_data()

# Création du menu paramètres de gauche
st.sidebar.header("Paramètres")
barchart_state = st.sidebar.radio('Répartition des doses', ['Cummulé', 'Juxtaposé'])

# Page centrale
st.title("Doses de Vaccins en Belgique", anchor="Center")

# Bar chart cumulé ou juxtaposé en fonction du paramètre
if barchart_state != "Cummulé":
    fig = px.histogram(d, x=d.index, y=["FirstDose", "SecondDose"], barmode='group', height=400)
    st.plotly_chart(fig, theme="streamlit", use_container_width=False, title="Dose by weeks (Plotly)")

else:
    fig = px.bar(d, height=400)
    st.plotly_chart(fig, theme="streamlit", use_container_width=False, title="Dose by weeks (Plotly)")

# Affichage des données en fonction du paramètre
with st.expander("Data"):
    st.header("Tableau des données")
    st.dataframe(d)



