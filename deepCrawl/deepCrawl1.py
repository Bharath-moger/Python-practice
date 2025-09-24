import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/"

# Step 1: Fetch the first page
url = "https://books.toscrape.com/catalogue/page-1.html"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Get all book links on that page
book_links = [a["href"] for a in soup.select("h3 a")]

# Step 3: Crawl into each book detail page
with open("deepCrawl.csv", "w", newline="", encoding="utf-8") as file:
             writer = csv.writer(file)
             writer.writerow(["Book Details"])
             for link in book_links:
                     full_link = base_url + link
                     res = requests.get(full_link, headers=headers)
                     detail_soup = BeautifulSoup(res.text, "html.parser")
                     title = detail_soup.find("h1").get_text()
                     price = detail_soup.find("p", class_="price_color").get_text()
                     stock = detail_soup.find("p", class_="instock availability").get_text(strip=True)
                     writer.writerow([f"Title: {title}\nPrice: {price}\nStock: {stock}\n{'-'*40}"])    
