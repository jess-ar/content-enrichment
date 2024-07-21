import logging
import requests
from src.utils import API_KEY

class TextImprover:
    def __init__(self):
        self.api_url = "https://api.textcortex.com/v1/texts/paraphrases"
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    def improve_text(self, text):
        if not text:
            return "Texto vacío no puede ser mejorado."

        try:
            payload = {
                "text": text
            }
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            logging.debug(f"Solicitud enviada a la API con payload: {payload}")
            response_data = response.json()
            logging.debug(f"Respuesta de la API: {response_data}")

            if response.status_code != 200:
                return f"Error: La API devolvió un código de estado {response.status_code}. Respuesta completa: {response_data}"

            if 'data' in response_data and 'outputs' in response_data['data']:
                improved_text = response_data['data']['outputs'][0]['text']
                return improved_text
            else:
                return f"Error: La estructura de la respuesta de la API no es válida. Respuesta completa: {response_data}"
        except Exception as e:
            logging.error(f"Error al mejorar el texto: {str(e)}")
            return f"Error al mejorar el texto: {str(e)}"
