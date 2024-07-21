from fpdf import FPDF
from src.Scraping import Scraping

class Generator (FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Arial", fname="C:/Windows/Fonts/Arial.ttf", uni=True)
        self.set_font("Arial", size=12)
    def texts (self,content):
        self.set_xy(10.0,80.0)
        self.set_text_color(0.0, 0.0, 0.0)
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)

    def titles(self,title):
        self.set_xy(10.0, 20.0)
        self.set_font("Arial", "B", 18)
        self.set_text_color(0.0, 0.0, 0.0)
        self.cell(w=210.0, h=40.0, align="c", txt=title, border=0)

    def generate_pdf(self, title, content, file_name):
        self.add_page()
        self.titles(title)
        self.texts(content)
        self.output(file_name, "F")

if __name__ == "__main__":
  try:

    search_query = "Python (programming language)"
    scraper = Scraping(search_query)
    title, content = scraper.scrape()

    pdf = Generator()
    file_name = "document.pdf"

    pdf.generate_pdf(title, content, file_name)

  except Exception as e:
      print(f"Ha ocurrido un error: {e}")