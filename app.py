import streamlit as st
from gtts import gTTS
import os
from io import BytesIO
from pydub import AudioSegment

# Configuration de l'application Streamlit
st.set_page_config(page_title="Générateur Audio IA", layout="centered")
st.title("🗣️ Générateur Audio avec IA")

# Entrée utilisateur
text = st.text_area("✍️ Entrez votre texte ici :", height=200)
voice_option = st.selectbox("🎙️ Choisissez une voix :", ["Homme", "Femme", "Enfant"])

# Mapping des langues/accents
voice_lang_map = {
    "Homme": "en",
    "Femme": "en",
    "Enfant": "en"
}

# Bouton pour générer l'audio
if st.button("🎬 Générer l'audio"):
    if not text.strip():
        st.warning("Veuillez entrer un texte valide.")
    else:
        with st.spinner("Génération en cours..."):
            lang = voice_lang_map[voice_option]
            tts = gTTS(text=text, lang=lang)

            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)

            audio = AudioSegment.from_file(audio_fp, format="mp3")
            audio_output = BytesIO()
            audio.export(audio_output, format="mp3")
            audio_output.seek(0)

            st.audio(audio_output, format='audio/mp3')
            st.download_button(
                label="🔹 Télécharger l'audio",
                data=audio_output,
                file_name="audio_ia.mp3",
                mime="audio/mp3"
            )
            st.success("Audio généré avec succès !")

st.markdown("---")
st.markdown("Créé par **TORIF** avec 🚀 et l'intelligence artificielle")
