# import requests
# from bs4 import BeautifulSoup   
# import time
# import csv

# base_url = "https://quotes.toscrape.com"

# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(base_url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# quotes_links = [a["href"] for a in soup.select("span a")]

# with open("deepCrawl.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Quotes Details"])
#     for link in quotes_links[10:22]:
#         full_link = base_url + link
#         res = requests.get(full_link, headers=headers)
#         detail_soup = BeautifulSoup(res.text, "html.parser")
#         quote_deatail = [[q.span.get_text(),q.small.get_text(),] for q in detail_soup.find_all("div", class_="quote")]
#         topics = detail_soup.find("h3").get_text(strip=True)
#         for i,[quote,author] in enumerate(quote_deatail,1):
#             writer.writerow([topics,i,quote,author])
#         # time.sleep(2)  # Be respectful to the server by adding a delay

import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor

base_url = "https://quotes.toscrape.com"

def scrape_page(link):
    full_link = base_url + link
    res = requests.get(full_link, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    topic = soup.find("h3").get_text(strip=True)
    quotes = [
        [q.span.get_text(), q.small.get_text()]
        for q in soup.find_all("div", class_="quote")
    ]
    return topic, quotes

# Step 1: collect links
res = requests.get(base_url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(res.text, "html.parser")
quotes_links = [a["href"] for a in soup.select("span a")][10:22]

# Step 2: fetch concurrently
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(scrape_page, quotes_links))

# Step 3: save CSV
with open("deepCrawl.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Topic", "SL No", "Quote", "Author"])
    for topic, quote_detail in results:
        for i, (quote, author) in enumerate(quote_detail, 1):
            writer.writerow([topic, i, quote, author])
