import logging
from src.Content_enrichment import ContentEnrichment

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def main():
    try:
        contentenrichment = ContentEnrichment()
        contentenrichment.run()
    except Exception as e:
        print(f"Error al ejecutar el programa: {e}")

if __name__ == "__main__":
    main()

