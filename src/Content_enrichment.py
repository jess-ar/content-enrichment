from src.Scraping import Scraping
from src.Gpt import TextImprover, GptService
from src.Translator import Translator
from src.utils import get_user_input, get_user_confirmation
from src.Generator import Generator

class ContentEnrichment:
    def __init__(self):
        self.text_improver = TextImprover()
        self.gpt_service = GptService(self.text_improver)
        self.translator = Translator()
        self.generator = Generator()

    def run(self):
        while True:
            search_term = get_user_input("Ingresa el tema de búsqueda: ")
            scraper = Scraping(search_term)
            title, content = scraper.scrape()

            if content:
                print(f"\nTítulo: {title}")
                print(f"Contenido:\n{content}")

                improved_content = content

                if get_user_confirmation("mejorar el texto"):
                    try:
                        improved_content = self.gpt_service.improve_wikipedia_text(content)
                        print(f"Texto Mejorado:\n{improved_content}")
                    except Exception as e:
                        print(f"Error al mejorar el texto: {e}")

                if get_user_confirmation("traducir el texto "):
                    src_lang = get_user_input("Ingresa el idioma de origen (ej. en): ")
                    tgt_lang = get_user_input("Ingresa el idioma de destino (ej. es): ")
                    try:
                        translated_content = self.translator.translate_text(improved_content, src_lang, tgt_lang)
                        print(f"Texto Traducido:\n{translated_content}")
                    except Exception as e:
                        print(f"Error al traducir el texto: {e}")

                    if get_user_confirmation("generar archivo PDF del texto traducido"):
                        file_name = "document.pdf"
                        change_name = get_user_input("¿Deseas cambiar el nombre del archivo? (s/n): ").strip().lower()
                        if change_name == "s":
                            file_name = get_user_input("Introduce el nuevo nombre del archivo(con extensión .pdf): ").strip()

                        try:
                            pdf = Generator()
                            pdf.generate_pdf(title, translated_content, file_name)
                            print(f"PDF generado con éxito: {file_name}")
                        except Exception as e:
                            print(f"Error al generar el PDF: {e}")


            else:
                print("No se encontró contenido para la búsqueda.")

            if not get_user_confirmation("realizar otra búsqueda"):
                print("Gracias por usar nuestra aplicacion. ¡Hasta la próxima!")
                break
