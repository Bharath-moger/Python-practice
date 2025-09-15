import requests
from bs4 import BeautifulSoup

url = "https://old.reddit.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text , "html.parser")

showName = [show.p.a.get_text() for show in soup.find_all("div",class_="top-matter")]

for i,show in enumerate(showName , 1):
    print(f"{i}. {show}")

# print(response)