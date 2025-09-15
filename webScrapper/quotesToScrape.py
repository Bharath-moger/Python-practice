import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/tag/humor/"
response = requests.get(url)

soup = BeautifulSoup(response.text , "html.parser")

quotes = [quote.span.get_text() for quote in soup.find_all("div",class_="quote")]

for i , quote in enumerate(quotes,1):
    print(f"{i}. {quote}")