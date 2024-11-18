import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Lecture de données Excel")
st.title("Pages : Pirate, Ship, Position")
st.subheader("Exemple de Merge de 3 tables")
# https://data.world/alexabayrome/pirate/workspace/file?filename=PirateData.xlsx
# Lecture du fichier Excel
sheets = pd.read_excel(R"piratedata.xlsx", sheet_name=["Pirate","Ship","Position"])

df = sheets["Pirate"].merge(sheets["Ship"], left_on='ShipID', right_on='ShipID', how='inner')
with st.expander("Ship"):
    st.table(df)

df = df.merge(sheets["Position"], left_on='PositionID', right_on='PositionID', how='inner')
print(df.info())
with st.expander("position"):
    st.table(df)

positions_gp = df.groupby(by="PositionName")["PositionID"].count()

with st.expander("Position"):
    st.table(positions_gp) 

st.bar_chart(positions_gp)

bar_colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'gold', 'yellow']
fig, ax = plt.subplots(figsize=(5,5))
ax.pie(positions_gp, 
        wedgeprops=dict(width=0.8), 
        startangle=-60, 
        labels=positions_gp.index, 
        autopct='%.1f%%',
        colors=bar_colors)
ax.set_title("title")
st.pyplot(fig)
