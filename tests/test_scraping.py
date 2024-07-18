import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Scraping import Scraping


def test_url_generation():
    scraper = Scraping("OpenAI")
    expected_url = "https://en.wikipedia.org/wiki/OpenAI"
    assert scraper.url == expected_url

def test_scrape(requests_mock):

    html_content = """
    <html>
    <head><title>Test Page</title></head>
    <body>
    <h1 class="firstHeading">Test Title</h1>
    <p>Paragraph 1.</p>
    <p>Paragraph 2.</p>
    <p>Paragraph 3.</p>
    <p>Paragraph 4.</p>
    <p>Paragraph 5.</p>
    <p>Paragraph 6.</p>
    </body>
    </html>
    """

    requests_mock.get("https://en.wikipedia.org/wiki/Test", text=html_content)
    scraper = Scraping("Test")
    title, content = scraper.scrape()
    assert title == "Test Title"
    expected_content = "Paragraph 1.\nParagraph 2.\nParagraph 3.\nParagraph 4.\nParagraph 5."
    assert content == expected_content
