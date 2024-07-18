import requests
from bs4 import BeautifulSoup

class Scraping:
    def __init__(self, search):
        self.search = search.replace(" ", "_")
        self.url = f"https://en.wikipedia.org/wiki/{self.search}"
        self.title = None
        self.content = None

    def scrape(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            self.title = soup.find("h1", {"class": "firstHeading"}).text.strip()
            paragraphs = soup.find_all("p")
            self.content = "\n".join([p.get_text(strip=True) for p in paragraphs[:5]])

        except requests.exceptions.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
        except Exception as err:
            print(f"Otro error: {err}")

        return self.title, self.content
