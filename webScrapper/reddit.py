import requests
from bs4 import BeautifulSoup
import csv

url = "https://old.reddit.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text , "html.parser")

showName = [show.p.a.get_text() for show in soup.find_all("div",class_="top-matter")]

with open("webscraper.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["S.No", "Today's Show"])   # header row
    for i,show in enumerate(showName , 1):
        writer.writerow([f"{i},{show}"])

