from deep_translator.exceptions import TranslationNotFound
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from Translator import Translator



def test_translate_text():
    translator = Translator()
    result = translator.translate_text('Hello', 'en', 'es')

    assert result == 'Hola'


def test_translate_text_not_found():
    translator = Translator()
    result = translator.translate_text('', 'en', 'es')
    assert not result == "Translation not found"