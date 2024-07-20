from fpdf import FPDF
from Scraping import Scraping

class Generator (FPDF):
    pass
    def texts (self,content):
        self.set_xy(10.0,80.0)
        self.set_text_color(0.0, 0.0, 0.0)
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)

    def titles(self,title):
        self.set_xy(0.0, 0.0)
        self.set_font("Arial", "B", 16)
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
    file_name = "output.pdf"
    change_name = input("¿Quieres cambiar el nombre del archivo? (s/n): ").strip().lower()
    if change_name == 's':
        file_name = input("Introduce el nuevo nombre del archivo (con extensión .pdf): ").strip()

    pdf.generate_pdf(title, content, file_name)

  except Exception as e:
      print(f"Ha ocurrido un error: {e}")