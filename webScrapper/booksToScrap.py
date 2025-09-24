import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract all book titles
titles = [[book.h3.a["title"],book.h3.a["href"]] for book in soup.find_all("article", class_="product_pod")]

# Print the titles
# file = open ('webscraper.csv',"w")
# for i, [title, href] in enumerate(titles, 1):
#     file.write(f"{i}. {title} :- {href}\n")
# file.close()
with open("webscraper.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["S.No", "Title", "Link"])   # header row
    for i, (title, href) in enumerate(titles, 1):
        writer.writerow([f"{i}. {title} :- \n {href}"])

