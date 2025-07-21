import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Générateur Audio IA", layout="centered")
st.title("🗣️ Générateur Audio avec IA")

text = st.text_area("✍️ Entrez votre texte ici :", height=200)
voice_option = st.selectbox("🎙️ Choisissez une voix :", ["Homme", "Femme", "Enfant"])

voice_lang_map = {
    "Homme": "fr",
    "Femme": "fr",
    "Enfant": "fr"
}

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

            st.audio(audio_fp, format='audio/mp3')
            st.download_button(
                label="⬇️ Télécharger l'audio",
                data=audio_fp,
                file_name="audio_ia.mp3",
                mime="audio/mp3"
            )
            st.success("Audio généré avec succès !")
