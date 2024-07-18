from deep_translator import (GoogleTranslator)
from deep_translator.exceptions import TranslationNotFound
class Translator :
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


"""esto es utils
        def get_user_input(prompt):
            return input(prompt)

        def display_output(output):
            return print(output)"""


"""esto es main

from src.utils import get_user_input , display_output
from src.Translator import Translator

text_input = get_user_input("ingresa un texto: ")
src_lang_input = get_user_input("tu lenguaje: ")
tgt_lang_input = get_user_input("lenguaje deseado: ")

translator_service = Translator()

translated = translator_service.translate_text(text_input, src_lang_input, tgt_lang_input)

display_output(translated)"""