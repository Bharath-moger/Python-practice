import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract all book titles
titles = [[book.h3.a["title"],book.h3.a["href"]] for book in soup.find_all("article", class_="product_pod")]

# Print the titles
for i, [title, href] in enumerate(titles, 1):
    print(f"{i}. {title} : {href}")  
# print(response) 