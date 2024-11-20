import pandas as pd
import streamlit as st

# Lecture et filtre du dataset
df = pd.read_csv("data.csv")
df = df.query('ReportingCountry == "BE"')
df = df.query('TargetGroup == "ALL"')
# Création de la table Pivot
#    Le contenu de la colonne "Vaccine" est le nom des nouvelles colonnes (AZ, COM, JANNSS, MOD)
#    Le contenu de la colonne "FirstDose" est sommé 
#    YearWeekISo est l'index de l'axe des X
df = df.pivot(index="YearWeekISO", 
              columns="Vaccine", 
              values="FirstDose")
st.title("Création de la table Pivot")
st.write("Vaccine sont les noms de colonnes (AZ, COM, JANNSS, MOD)")
st.write("FirstDose sont les sommes des valeurs des colonnes")
st.write("YearWeekISo est l'index de l'axe des X")
st.line_chart(df)
st.write(df)