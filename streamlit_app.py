import streamlit as st

st.set_page_config(page_title="Generateur de CV", page_icon="📄")

st.title("Generateur de CV Professionnel")
st.write("Remplissez et telechargez votre CV")

nom = st.text_input("Nom et Prenom *")
email = st.text_input("Email *")
telephone = st.text_input("Telephone")
formation = st.text_area("Formation *")
competences = st.text_area("Competences")
projets = st.text_area("Projets")
experience = st.text_area("Experience")

if st.button("Generer le CV"):
    if nom and email and formation:
        cv_text = f"""
CV DE {nom.upper()}

Email: {email}
Telephone: {telephone}

FORMATION

{formation}

COMPETENCES

{competences}

PROJETS

{projets}

EXPERIENCE

{experience}
"""
        st.success("CV genere avec succes!")
        st.download_button(
            label="📄 Telecharger CV.txt",
            data=cv_text,
            file_name=f"CV_{nom}.txt",
            mime="text/plain"
        )
    else:
        st.error("Remplissez Nom, Email et Formation")
