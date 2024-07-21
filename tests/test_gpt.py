import pytest
from src.Gpt import TextImprover

# Test para la mejora de un texto válido
def test_improve_valid_text():
    # Given
    text_improver = TextImprover()
    text = "Vigo is a city and municipality in the province of Pontevedra, within the autonomous community of Galicia, Spain."

    # When
    result = text_improver.improve_text(text)

    # Then
    # Verifica que el texto mejorado contiene palabras clave importantes
    assert "Vigo" in result, f"Expected 'Vigo' to be in the improved text, but got: {result}"
    assert "city" in result, f"Expected 'city' to be in the improved text, but got: {result}"
    assert "Pontevedra" in result, f"Expected 'Pontevedra' to be in the improved text, but got: {result}"
    assert "Galicia" in result, f"Expected 'Galicia' to be in the improved text, but got: {result}"

# Test para manejar el caso de un texto vacío
def test_improve_empty_text():
    # Given
    text_improver = TextImprover()
    text = ""

    # When
    result = text_improver.improve_text(text)

    # Then
    assert result == "Texto vacío no puede ser mejorado.", f"Expected error message, but got: {result}"