mport streamlit as st

st.set_page_config(page_title="Générateur de CV avec IA", layout="centered")

st.title("📄 Générateur de CV avec IA")
st.write("دخل المعلومات ديالك و غيعطيك CV بالفرنسية واجد للنسخ")

col1, col2 = st.columns(2)
with col1:
    nom = st.text_input("Nom et Prénom *")
    diplome = st.text_input("Diplôme *")
with col2:
    email = st.text_input("Email")
    telephone = st.text_input("Téléphone")

experience = st.text_area("Expérience professionnelle", height=150)
competences = st.text_input("Compétences", placeholder="Ex: Word, Excel, Anglais, Python")

if st.button("✨ Générer mon CV"):
    if nom and diplome:
        cv_texte = f"""
{nom}
{email} | {telephone}

PROFIL
Jeune diplômé(e) motivé(e) à la recherche d'une opportunité pour mettre en pratique mes compétences.

FORMATION
{diplome}

EXPÉRIENCE PROFESSIONNELLE
{experience}

COMPÉTENCES
{competences}
        """
        st.success("✅ Voilà votre CV!")
        st.text_area("Copiez votre CV ici", cv_texte, height=400)
        st.info("💡 Dير Ctrl+A باش تحدد الكل > Ctrl+C > الصقو فـ Word")
    else:
        st.error("Merci de remplir Nom et Diplôme *")
