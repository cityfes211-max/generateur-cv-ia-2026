import streamlit as st

st.set_page_config(page_title="Générateur de CV avec IA", layout="centered")

st.title("📄 Générateur de CV avec IA")
st.write("دخل المعلومات ديالك و غيعطيك CV بالفرنسية واجد")

nom = st.text_input("Nom et Prénom")
diplome = st.text_input("Diplôme")
experience = st.text_area("Expérience professionnelle")
competences = st.text_input("Compétences")

if st.button("✨ Générer mon CV"):
    if nom and diplome:
        cv = f"""CV de {nom}

DIPLÔME
{diplome}

EXPÉRIENCE
{experience}

COMPÉTENCES
{competences}
        """
        st.success("Voilà votre CV!")
        st.text_area("Votre CV", cv, height=400)
    else:
        st.warning("Merci de remplir au moins Nom et Diplôme")
