from deep_translator.exceptions import TranslationNotFound
from src.Translator import Translator



def test_translate_text():
    translator = Translator()
    result = translator.translate_text('Hello', 'en', 'es')

    assert result == 'Hola'


def test_translate_text_not_found():
    translator = Translator()
    result = translator.translate_text('', 'en', 'es')

    assert result == "Translation not found"