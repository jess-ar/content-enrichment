import pytest
import sys
import os
from transformers import AutoTokenizer

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Gpt import TextImprover, GptService


class MockModel:
    def generate(self, input_ids, max_length, num_return_sequences):
        return [[token_id for token_id in input_ids[0]] + [42]]


@pytest.fixture
def text_improver():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = MockModel()
    text_improver = TextImprover()
    text_improver.tokenizer = tokenizer
    text_improver.model = model
    return text_improver


@pytest.fixture
def gpt_service(text_improver):
    return GptService(text_improver)


def test_improve_text(text_improver):
    text = "El método mejora efectivamente un texto"
    result = text_improver.improve_text(text)
    print(result)
    assert result != text


def test_improve_text_empty(text_improver):
    text = ""
    result = text_improver.improve_text(text)
    print(result)
    assert result == "Texto vacío no puede ser mejorado."

def test_improve_text_special_chars(text_improver):
    text = "!@#$$%^&*()Se maneja correctamente un texto compuesto de caracteres especiales"
    result = text_improver.improve_text(text)
    print(result)
    assert result != text


def test_improve_wikipedia_text(gpt_service):
    text = "el servicio GptService mejora el texto utilizando improve_text de TextImprover."
    result = gpt_service.improve_wikipedia_text(text)
    print(result)
    assert result != text

def test_improve_text_with_long_input(text_improver):
    text = " ".join(["word"] * 1000)  # Texto largo
    result = text_improver.improve_text(text)
    print(result)
    assert result != text
    assert len(result) > len(text)


def test_improve_text_error_handling(monkeypatch, text_improver):
    def mock_generate(*args, **kwargs):
        raise RuntimeError("Error en el modelo")

    monkeypatch.setattr(text_improver.model, 'generate', mock_generate)

    text = "Simula un error en la generación de texto y asegura que el sistema maneje este error adecuadamente"
    result = text_improver.improve_text(text)
    print(result)
    assert result == "Error al mejorar el texto: Error en el modelo"


def test_improve_text_format(text_improver):
    text = "Verifica que el texto mejorado tenga el formato correcto (es decir, no esté vacío ni compuesto solo por espacios"
    result = text_improver.improve_text(text)
    print(result)
    assert isinstance(result, str)
    assert result.strip() != ""  # El resultado no debe estar vacío o solo ser espacios