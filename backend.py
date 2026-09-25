from deep_translator import GoogleTranslator

class TranslationBackend:
    def __init__(self):
        self.supported_languages = {
            "Auto Detect": "auto",
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese (Simplified)": "zh-CN",
            "Chinese (Traditional)": "zh-TW",
            "Russian": "ru",
            "Portuguese": "pt",
            "Hindi": "hi",
            "Arabic": "ar",
            "Dutch": "nl",
            "Polish": "pl",
            "Turkish": "tr"
        }

    def get_supported_languages(self):
        """Returns dictionary of supported input languages including Auto Detect."""
        return self.supported_languages

    def get_target_languages(self):
        """Returns list of output languages (excluding Auto Detect)."""
        return [lang for lang in self.supported_languages.keys() if lang != "Auto Detect"]

    def get_word_and_char_count(self, text):
        """Calculates word and character counts for the given text."""
        if not text:
            return 0, 0
        words = len(text.strip().split())
        chars = len(text)
        return words, chars

    def translate_text(self, text, source_label, target_label):
        """Translates text from source_label language to target_label language using deep_translator."""
        if not text or not text.strip():
            return "", None

        try:
            source_code = self.supported_languages.get(source_label, "auto")
            target_code = self.supported_languages.get(target_label, "en")

            translator = GoogleTranslator(source=source_code, target=target_code)
            translated = translator.translate(text)
            return translated, None
        except Exception as e:
            return "", f"Translation error: {str(e)}"
