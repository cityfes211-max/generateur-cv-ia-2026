import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(page_title="Générateur de CV avec IA", layout="centered")

st.title("📄 Générateur de CV avec IA")
st.write("دخل المعلومات ديالك و غيعطيك CV بالفرنسية واجد للتحميل")

col1, col2 = st.columns(2)
with col1:
    nom = st.text_input("Nom et Prénom *")
    diplome = st.text_input("Diplôme *")
with col2:
    email = st.text_input("Email")
    telephone = st.text_input("Téléphone")

experience = st.text_area("Expérience professionnelle", height=150, 
                          placeholder="Stage - Entreprise - Dates\n- Mission 1\n- Mission 2")
competences = st.text_input("Compétences", placeholder="Python, Word, Excel, Anglais")

def creer_pdf(nom, diplome, email, telephone, experience, competences):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(200, 10, txt=f"CV de {nom}", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"{email} | {telephone}", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt="DIPLOME", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, txt=diplome)
    pdf.ln(3)
    
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt="EXPERIENCE PROFESSIONNELLE", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, txt=experience)
    pdf.ln(3)
    
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt="COMPETENCES", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, txt=competences)
    return pdf.output(dest='S').encode('latin-1')

if st.button("✨ Générer mon CV"):
    if nom and diplome:
        cv_texte = f"""CV de {nom}
Email: {email} | Tel: {telephone}

DIPLÔME
{diplome}

EXPÉRIENCE
{experience}

COMPÉTENCES
{competences}
        """
        st.success("Voilà votre CV!")
        st.text_area("Aperçu du CV", cv_texte, height=400)
        
        # زر التحميل
        pdf_bytes = creer_pdf(nom, diplome, email, telephone, experience, competences)
        b64 = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{nom}_CV.pdf">📥 Télécharger mon CV en PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.error("Merci de remplir Nom et Diplôme *")
