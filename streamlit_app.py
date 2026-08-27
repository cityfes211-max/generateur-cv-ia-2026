import streamlit as st

st.set_page_config(page_title="Generateur de CV", page_icon="📄")

st.title("Generateur de CV Professionnel")
st.write("Remplissez et telechargez votre CV en PDF")

nom = st.text_input("Nom et Prenom *")
email = st.text_input("Email *")
telephone = st.text_input("Telephone")
formation = st.text_area("Formation *")
competences = st.text_area("Competences")
projets = st.text_area("Projets")
experience = st.text_area("Experience")

if st.button("Generer le CV"):
    if nom and email and formation:
        cv_html = f"""
        <h1 style='text-align:center'>{nom.upper()}</h1>
        <p style='text-align:center'>{email} | {telephone}</p><hr>
        <h3>FORMATION</h3><p>{formation}</p>
        <h3>COMPETENCES</h3><p>{competences}</p>
        <h3>PROJETS</h3><p>{projets}</p>
        <h3>EXPERIENCE</h3><p>{experience}</p>
        """
        st.markdown(cv_html, unsafe_allow_html=True)
        st.download_button(
            label="📄 Telecharger en PDF",
            data=cv_html,
            file_name=f"CV_{nom}.html",
            mime="text/html"
        )
        st.info("Astuce: Ouvrez le fichier .html avec Word puis Enregistrer en PDF")
    else:
        st.error("Remplissez Nom, Email et Formation")
