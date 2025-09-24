import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/tag/humor/"
response = requests.get(url)

soup = BeautifulSoup(response.text , "html.parser")

quotes = [quote.span.get_text() for quote in soup.find_all("div",class_="quote")]

with open("webscraper.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quotes Are:"])   # header row
    for i, quote in enumerate(quotes, 1):
        writer.writerow([f"{i},{quote}"])