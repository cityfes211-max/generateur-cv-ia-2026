import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Generateur de CV", page_icon="📄")

st.title("Generateur de CV Professionnel")
st.write("Remplissez le formulaire et telechargez votre CV")

nom = st.text_input("Nom et Prenom *")
email = st.text_input("Email *")
formation = st.text_area("Formation *")
competences = st.text_area("Competences")
projets = st.text_area("Projets")
experience = st.text_area("Experience")

if st.button("Generer le CV"):
    if nom and email and formation:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, nom.upper(), 0, 1, "C")
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"{email}", 0, 1, "C")
        pdf.ln(5)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "FORMATION", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, formation)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "COMPETENCES", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, competences)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "PROJETS", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, projets)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "EXPERIENCE", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, experience)
        
        pdf.output("CV.pdf")
        st.success("CV genere avec succes!")
        with open("CV.pdf", "rb") as f:
            st.download_button("Telecharger PDF", f, "CV.pdf")
    else:
        st.error("Remplissez Nom, Email et Formation")
