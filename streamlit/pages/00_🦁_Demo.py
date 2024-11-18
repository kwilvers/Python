import streamlit as st
import pandas as pd

st.title("Démo de Streamlit")
df = pd.read_csv("Animals.csv", sep=",")
df.info()

selectedClass = st.sidebar.selectbox("Sélectionner classe taxonomique", df["TaxonClass"].unique())

df = df.query("TaxonClass == @selectedClass")

if st.sidebar.checkbox("Supprimer NULL"):
    df = df.query('`Male Data Deficient`.notnull()', engine='python')

with st.expander("Data Table"):
    st.table(df)

st.bar_chart(df, x="Species Common Name", y="Overall Sample Size")