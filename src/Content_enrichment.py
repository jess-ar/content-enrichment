from src.utils import get_user_input, get_user_confirmation
from src.Scraping import Scraping
# se deben importar los de mas clases


# se debe verificar el clase Content_enrichment
class Content_enrichment:
    def __init__(self):
        self.scraper = None

    def run(self):
        search = get_user_input("Ingreas una tema para buscar: ")
        self.scraper = Scraping(search)
        title, content = self.scraper.scrape()

        if title and content:
            print(f"Título del artículo: {title}\n")
            print("Contenido:")
            print(content)
        else:
            print("No se encontró contenido para el término de búsqueda.")


