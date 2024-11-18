import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import ticker
import matplotlib.pyplot as plt

# Fonction de création d'un Piechart
def createPieChart(colors, column, title, figSize = (5,5)):
    fig, ax = plt.subplots(figsize=figSize)
    ax.pie(d[column], 
           wedgeprops=dict(width=0.8), 
           startangle=-60, 
           labels=d.index, 
           autopct='%.1f%%',
           colors=colors)
    ax.set_title(title)
    ax.legend(["Astra", "Pfizer", "Jansen", "Moderna"])
    st.pyplot(fig)

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
show_data = st.sidebar.checkbox('Afficher les données')

# Page centrale
st.title("Doses de Vaccins en Belgique", anchor="Center")

# Bar chart cumulé ou juxtaposé en fonction du paramètre
if barchart_state != "Cummulé":
    width = 0.5
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(d.index, d["FirstDose"], width=width)
    ax.bar(np.arange(len(d["SecondDose"]))+width, d["SecondDose"], width=width)
    ax.legend(["FirstDose", "SecondDose"], bbox_to_anchor=(1,1), loc="upper left")
    ax.ticklabel_format(axis="y", style="plain", useLocale=True)
    ax.grid(axis='y')
    st.pyplot(fig)
else:
    st.bar_chart(d, width=0.3)

# Affichage des données en fonction du paramètre
if show_data:
    st.header("Tableau des données")
    st.dataframe(d)

# Pie chart de répartition des doses
st.header("Répartition des doses")
col1, col2 = st.columns(2)
with col1:
    createPieChart(['red', 'darkred', 'firebrick', 'pink'], "FirstDose", 'First doses')

with col2:
    createPieChart(['royalblue', 'Teal', 'lightblue', 'cyan'], "SecondDose", 'Second doses')

    

