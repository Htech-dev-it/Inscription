import streamlit as st
from PIL import Image
import base64
import io


# Fonction pour convertir une image en base64
def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


# Configuration de la page
st.set_page_config(
    page_title="École Les Taïnos – Inscriptions 2025–2026",
    layout="wide"
)

# Chargement du logo
logo = Image.open("logo.png")
logo_base64 = image_to_base64(logo)

# Appliquer un fond de page personnalisé
st.markdown("""
    <style>
    body, .main, .block-container {
        background-color: #0C142F !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Cache le menu des trois points en haut à droite */
    #MainMenu {visibility: hidden;}

    /* Cache le footer "Made with Streamlit" */
    footer {visibility: hidden;}

    /* Rendre visible le header Streamlit */
    header {visibility: visible;}
    </style>
""", unsafe_allow_html=True)

# Bannière large avec contenu centré
st.markdown(f"""
    <style>
    .header-container {{
        background-color: #D6EAF8;
        border-radius: 16px;
        padding: 40px 20px;
        margin-bottom: 30px;
        width: 100%;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}
    .header-content {{
        max-width: 1000px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .header-logo {{
        margin-right: 20px;
    }}
    .header-text h1 {{
        font-size: 60px;
        margin: 0;
        color: #154360;
    }}
    .header-text h3 {{
        font-size: 32px;
        margin: 5px 0 0;
        color: #1A5276;
    }}
    @media (max-width: 768px) {{
        .header-content {{
            flex-direction: column;
            text-align: center;
        }}
        .header-logo {{
            margin: 0 0 20px 0;
        }}
    }}
    </style>

    <div class="header-container">
        <div class="header-content">
            <div class="header-logo">
                <img src="data:image/png;base64,{logo_base64}" width="100">
            </div>
            <div class="header-text">
                <h1>École « Les Taïnos »</h1>
                <h3>Inscriptions 2025 – 2026</h3>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Largeur personnalisée
st.markdown("""
    <style>
    .main .block-container {
        max-width: 95%;
        padding-left: 5%;
        padding-right: 5%;
    }
    .section-title {
        font-size: 36px;
        color: white;
        background-color: #2E86C1;
        padding: 20px;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        margin-top: 40px;
        margin-bottom: -10px;
    }
    .section-content {
        font-size: 26px;
        line-height: 2;
        color: black;
        background-color: #F4F6F6;
        padding: 30px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 📍 Coordonnées
st.markdown("<div class='section-title'>📍 Coordonnées</div>", unsafe_allow_html=True)
st.markdown("""
<div class='section-content'>
<b>Adresse :</b> 1, Rue Marcel Toureau, Morne Brun, Berthé – Pétion-Ville (Haïti)<br>
<b>Email :</b> collegelestainos@yahoo.fr<br>
<b>Téléphones :</b> 38 45 00 99 / 34 03 16 09
</div>
""", unsafe_allow_html=True)

# 🎓 Présentation
st.markdown("<div class='section-title'>🎓 Présentation de l’établissement</div>", unsafe_allow_html=True)
st.markdown("""
<div class='section-content'>
✅ Programmes basés sur les systèmes <b>français</b> et <b>haïtien</b><br>
✅ Plateforme d’enseignement <b>à distance</b> disponible<br>
✅ Cadre <b>chaleureux, agréable et sécurisé</b><br>
✅ Groupes à <b>effectif limité</b><br>
✅ Dirigée par <b>Hélène Ney-Pierre Laraque</b>
</div>
""", unsafe_allow_html=True)

# 📅 Inscriptions
st.markdown("<div class='section-title'>📅 Inscriptions 2025 – 2026</div>", unsafe_allow_html=True)
st.markdown("""
<div class='section-content'>
<b>Classes concernées :</b> De 1AF à 6AF<br>
<b>Date de début :</b> À partir du <b style="color:green;">mercredi 8 janvier 2025</b>
</div>
""", unsafe_allow_html=True)

# 📑 Pièces à fournir
st.markdown("<div class='section-title'>📑 Pièces à fournir</div>", unsafe_allow_html=True)
st.markdown("""
<div class='section-content'>
📄 Acte de naissance<br>
📘 Dernier bulletin scolaire (année 2024–2025)<br>
💉 Carnet de vaccination<br>
🖼️ 2 photos d’identité récentes<br>
💵 60 dollars US (frais de dossier et d’examen)
</div>
""", unsafe_allow_html=True)

# 📝 Examen
st.markdown("<div class='section-title'>📝 Examen d’admission</div>", unsafe_allow_html=True)
st.markdown("""
<div class='section-content'>
L’examen d’entrée est organisé <b>sur rendez-vous</b>.<br>
📞 Merci de nous contacter au <b>34 03 16 09</b> pour fixer une date.
</div>
""", unsafe_allow_html=True)

# 🎉 Message final
st.markdown(
    "<div class='section-content' style='text-align: center; border-top-left-radius: 10px; border-top-right-radius: 10px; margin-top:55px; font-size: 30px; background-color: #D5F5E3;'>🎉 Rejoignez une école d’excellence dès aujourd’hui !</div>",
    unsafe_allow_html=True)
