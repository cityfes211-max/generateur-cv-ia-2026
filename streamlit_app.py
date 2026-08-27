import streamlit as st
from fpdf import FPDF
import io

st.set_page_config(page_title="Générateur de CV", page_icon="📄", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Générateur de CV Professionnel</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Remplissez les informations et téléchargez votre CV en PDF</p>", unsafe_allow_html=True)

with st.form("cv_form"):
    st.subheader("1. Informations Personnelles")
    nom = st.text_input("Nom et Prénom *")
    email = st.text_input("Email *")
    telephone = st.text_input("Téléphone")
    
    st.subheader("2. Formation")
    formation = st.text_area("Votre Formation *", placeholder="Ex: Baccalauréat Sciences Mathématiques - Lycée XYZ, 2023-2026")
    
    st.subheader("3. Compétences")
    competences = st.text_area("Vos Compétences", placeholder="Ex: Python, Streamlit, Français, Anglais")
    
    st.subheader("4. Projets")
    projets = st.text_area("Vos Projets", placeholder="Ex: Générateur de CV avec IA - Application web pour créer des CV")
    
    st.subheader("5. Expérience")
    experience = st.text_area("Expérience / Stages", placeholder="Ex: Stage d'observation - Entreprise ABC")
    
    submitted = st.form_submit_button("✨ Générer mon CV")

if submitted:
    if nom == "" or email == "" or formation == "":
        st.error("Veuillez remplir les champs obligatoires: Nom, Email, Formation")
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt=nom.upper(), ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.cell(200, 10, txt=f"{email} | {telephone}", ln=True, align="C")
        pdf.ln(10)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="FORMATION", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, txt=formation)
        pdf.ln(5)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="COMPETENCES", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, txt=competences)
        pdf.ln(5)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="PROJETS", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, txt=projets)
        pdf.ln(5)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, txt="EXPERIENCE", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, txt=experience)
        
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        
        st.success("Votre CV est prêt !")
        st.download_button(
            label="📄 Télécharger en PDF",
            data=pdf_bytes,
            file_name=f"CV_{nom}.pdf",
            mime="application/pdf"
        )
