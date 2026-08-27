import streamlit as st
from fpdf import FPDF

# --- 1. التصميم + الألوان ---
st.set_page_config(page_title="Générateur CV IA", layout="centered")

st.markdown("""
<style>
    .main-title {color: #4F8BF9; font-size: 32px; font-weight: bold; text-align: center;}
    .subtitle {color: #555; font-size: 16px; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📄 Générateur de CV avec IA</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle"><b>Créez votre CV professionnel en 2 minutes avec l\'IA</b></p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle"><i>بإمكانك الآن إنشاء سيرتك الذاتية بالذكاء الاصطناعي في دقائق</i></p>', unsafe_allow_html=True)

st.divider()

# --- 2. الخيارات الكثيرة ---
col1, col2 = st.columns(2)

with col1:
    nom = st.text_input("Nom et Prénom *")
    email = st.text_input("Email *")
    telephone = st.text_input("Téléphone")
    poste = st.text_input("Poste visé *", placeholder="Ex: Développeur Python")

with col2:
    formation = st.text_area("Formation *", placeholder="Ex: Bac Sciences Maths, Lycée XYZ")
    langues = st.text_input("Langues *", "Français, Arabe, Anglais")
    template = st.selectbox("Choisir un modèle de CV", ["Moderne", "Classique", "Créatif"])

experience = st.text_area("Expérience professionnelle", placeholder="Ex: Stage de 2 mois en développement web...")
competences = st.text_input("Compétences *", "Python, SQL, Communication")

# --- 3. دالة توليد PDF ---
def creer_pdf(nom, email, tel, poste, formation, langues, exp, comp):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"CV - {nom}", ln=True, align='C')
    pdf.set_font("Arial", size=11)
    pdf.ln(5)
    pdf.cell(200, 8, txt=f"Email: {email} | Tel: {tel}", ln=True)
    pdf.cell(200, 8, txt=f"Poste vise: {poste}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, txt="FORMATION", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, txt=formation)
    pdf.ln(2)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, txt="EXPERIENCE", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, txt=exp)
    pdf.ln(2)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, txt="COMPETENCES & LANGUES", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 8, txt=f"Competences: {comp}", ln=True)
    pdf.cell(200, 8, txt=f"Langues: {langues}", ln=True)
    
    return pdf.output(dest='S').encode('latin-1')

# --- 4. الزر + التحميل ---
if st.button("✨ Générer mon CV", type="primary", use_container_width=True):
    if nom and email and poste and formation:
        with st.spinner("L'IA génère votre CV..."):
            pdf_bytes = creer_pdf(nom, email, telephone, poste, formation, langues, experience, competences)
        
        st.success("✅ Votre CV est prêt!")
        st.download_button(
            label="📄 Télécharger en PDF",
            data=pdf_bytes,
            file_name=f"CV_{nom.replace(' ', '_')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.error("Merci de remplir les champs obligatoires *")
