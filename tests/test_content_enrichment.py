import pytest
import requests_mock
from src.Gpt import TextImprover
from src.Content_enrichment import ContentEnrichment

@pytest.fixture
def text_improver():
    return TextImprover()

@pytest.fixture
def content_enrichment():
    return ContentEnrichment()

@pytest.fixture
def mock_api():
    with requests_mock.Mocker() as m:
        url = "https://api.textcortex.com/v1/texts/paraphrases"
        response = {
            "status": "success",
            "data": {
                "outputs": [
                    {
                        "index": 0,
                        "text": "Vigo, a thriving city in the province of Pontevedra, Galicia, Spain, sits along the Ria de Vigo."
                    }
                ],
                "remaining_credits": 4.88828
            }
        }
        m.post(url, json=response)
        yield m

def test_improve_text(text_improver, mock_api):
    # Given
    text = "Vigo is a city and municipality in the province of Pontevedra, within the autonomous community of Galicia, Spain."

    # When
    result = text_improver.improve_text(text)

    # Then
    assert result == "Vigo, a thriving city in the province of Pontevedra, Galicia, Spain, sits along the Ria de Vigo.", f"Expected improved text, but got: {result}"
    assert mock_api.called, "Expected API to be called, but it was not."
    assert mock_api.call_count == 1, f"Expected 1 call to API, but got: {mock_api.call_count}"

def test_handle_empty_text(text_improver):
    # Given
    text = ""

    # When
    result = text_improver.improve_text(text)

    # Then
    assert result == "Texto vacío no puede ser mejorado.", f"Expected error message, but got: {result}"