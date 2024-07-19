from deep_translator import (GoogleTranslator)
from deep_translator.exceptions import TranslationNotFound
class Translator:
    def __init__(self):
        pass

    def translate_text(self, text, src_lang, tgt_lang):
        try:
            translated_text = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
            return translated_text
        except TranslationNotFound:
            return "Translation not found"
        except Exception as e:
            return f"An unexpected error was found: {e}"


