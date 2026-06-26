import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Translator App", page_icon="🌍")

st.title("🌍 Smart Language Translator")
st.write("Translate text easily between multiple languages")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Urdu": "ur"
}

source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    
    if source_lang == target_lang:
        st.warning("⚠ Source and Target language cannot be same!")

    elif not text:
        st.warning("⚠ Please enter text!")

    else:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("✅ Translated Text:")
        st.write(translated)

        st.download_button(
            label="📥 Download Translation",
            data=translated,
            file_name="translation.txt"
        )