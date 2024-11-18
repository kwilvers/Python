import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Lecture de données Excel")
st.subheader("Affichage de graphique Matplotlib")

# https://data.world/alexabayrome/pirate/workspace/file?filename=PirateData.xlsx
# Lecture du fichier CSV
df = pd.read_excel(R"piratedata.xlsx", sheet_name="Pirate")
# récupération des origines des pirates de manière unique
origins = df["Origin"].unique()

st.sidebar.title("Filtres :")
origin = st.sidebar.selectbox("Origin : ", origins)
pirates = df.query(f"Origin == '{origin}'")

nb_teeth = st.sidebar.select_slider("Nombre de dents :", sorted(pirates["Teeth"].unique()))
pirates = pirates.query(f"Teeth == {nb_teeth}")

with st.expander("Pirates"):
    st.table(pirates)


dforigin = df.query(f"Origin == '{origin}'")
gp_teeths = dforigin.groupby(by="Teeth").count()
with st.expander("Dents"):
    st.table(gp_teeths) 

st.bar_chart(gp_teeths["Origin"])

dfByOrigin = df.groupby("Origin").count()

with st.expander("Origin"):
    st.table(dfByOrigin) 
st.bar_chart(dfByOrigin["Teeth"])


fig, ax = plt.subplots(figsize=(10,5))
bar_colors = ['red', 'blue', 'green', 'orange', 'purple']
ax.bar(dfByOrigin.index, dfByOrigin["Teeth"],  color=bar_colors)
ax.grid(axis='y')
ax.set_xticks(dfByOrigin.index)
ax.set_xticklabels(dfByOrigin.index, rotation=90)

st.pyplot(fig)


