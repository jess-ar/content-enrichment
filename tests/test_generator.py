import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.Generator import Generator
def test_Generator():
    pdf = Generator()
    initial_page_count = len(pdf.pages)
    pdf.add_page()
    assert len(pdf.pages) == initial_page_count + 1


def test_generate_files():
    pdf = Generator()
    title = "Test Title"
    content = "Test Content"
    file_name = "test_output.pdf"
    pdf.generate_pdf(title, content, file_name)
    assert os.path.isfile(file_name)
    os.remove(file_name)
