import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# 🍿 Améliorer la solution ! 🍿")

st.sidebar.success("Click sur une démo ci-dessus")

st.markdown( """
        ## 📑 Mode multipages
        Pour Utiliser le mode page, il s'uffit de créer un répertoire **pages** et de déplacer vos scripts dans le répertoire page.
        Streamlit va alors créer une zone de sélection de la page 😌
        
        Plus de détail ici : https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app

        ## Icones 🐵 🦄 🦁
        https://emojis.wiki/fr/ogre/

        Pour ajouter une icone ajouter l'icone dans le nom de fichier
   """)

st.image("./Directory.png", width=400)
