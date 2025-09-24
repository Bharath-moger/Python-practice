import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://news.ukexpress.in/"
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')
for headline in soup.find_all('div', class_='p-4 sm:p-6'):
    h3 = headline.find('h3')
    if h3:   # only add if <h2> exists
        print(h3.get_text(strip=True))
    else:
        print("No headline found")