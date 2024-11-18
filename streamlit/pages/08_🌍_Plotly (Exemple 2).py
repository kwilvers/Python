import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache_data
def load_data():
    #Ajouter un spinner
    with st.spinner(text='Reading data...'):
        df = pd.read_csv(R".\data.csv")
        # Filter weeks
        weeks = pd.Series(sorted(df["YearWeekISO"].unique()))
        #Filter countries
        countries = df["ReportingCountry"].unique()
    return (df, weeks, countries)


# Chargement des données en cache
d, weeks, countries = load_data()

# Slider ou checkbo paramètres de date
st.sidebar.header("Paramètres") 

# Filtre par range de date
begin = st.sidebar.select_slider("Date de début", weeks, value=weeks.min())
end = st.sidebar.select_slider("Date de fin", weeks, value=weeks.max())
d = d.query(f"YearWeekISO >= '{begin}'")
d = d.query(f"YearWeekISO <= '{end}'")

# Filtre sur le pays
id_be = int(np.argwhere(countries == "BE")[0][0])
country = st.sidebar.selectbox("Pays", countries, index=id_be)
d = d.query(f'ReportingCountry == "{country}"')

#Filtre tranche d'ages
# Obtenir la liste des tranches d'ages
targetgroups = d["TargetGroup"].unique()
#tg = st.sidebar.multiselect('Age', targetgroups, default="ALL")
tg = st.sidebar.multiselect('Age', targetgroups, default=targetgroups)
d = d[d.TargetGroup.isin(tg)]

# Group by par semaine
d = d.groupby(by = "YearWeekISO")
d = d[["FirstDose","SecondDose"]].sum()

# Calcul des moyennes
meanFirst = d["FirstDose"].mean()
meanSecond = d["SecondDose"].mean()

# Ajout des colonnes moyennes
d = d.assign(meanFirst = [meanFirst for i in range(len(d))])
d = d.assign(meanSecond = [meanSecond for i in range(len(d))])

st.header("Dose by weeks (Plotly)")

#fig = px.line(d, facet_row="company", facet_row_spacing=0.01, height=200, width=200)
fig = px.line(d)
st.plotly_chart(fig, theme="streamlit", use_container_width=False, title="Dose by weeks (Plotly)")






