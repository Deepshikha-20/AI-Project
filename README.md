# 🌐 PolyGlot AI Translator

A seamless, fast, and interactive text translation application built with Python and Streamlit. This app uses `deep-translator` under the hood to provide accurate translations across a variety of supported languages with a clean, dual-pane UI.

## ✨ Features

- **Dual-Pane Interface:** Clean and intuitive UI featuring side-by-side source and target text areas.
- **Auto-Detection:** Automatically detect the input language for effortless translations.
- **Real-Time Text Stats:** Live word and character counting for the source text.
- **Wide Language Support:** Supports multiple languages including English, Spanish, French, German, Italian, Japanese, Korean, Chinese, Russian, Portuguese, Hindi, Arabic, and more.
- **Instant Translation:** Automatically translates as you type/paste the text.

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **Backend Translation:** [deep-translator](https://pypi.org/project/deep-translator/) (`GoogleTranslator`)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Deepshikha-20/AI-Project.git
   cd AI-Project
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed. Then, run:
   ```bash
   pip install streamlit deep-translator
   ```

3. **Run the application:**
   ```bash
   streamlit run Fronted.py
   ```

## 📂 Project Structure

- `Fronted.py`: The main Streamlit application file handling the UI/UX and user interactions.
- `backend.py`: The backend logic for the translator, bridging the UI with the `deep-translator` package and handling text statistics.
- `.gitignore`: Files ignored by git (e.g., Python `__pycache__`).

## 💡 Usage Tip
Selecting **"Auto Detect"** in the Source language dropdown allows the backend to automatically identify the input language, saving you time when translating unknown text.
