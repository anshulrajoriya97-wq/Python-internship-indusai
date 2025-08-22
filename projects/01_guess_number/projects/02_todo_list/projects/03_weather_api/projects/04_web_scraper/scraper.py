import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print(f"📑 Titles from {url}:")
    for i, title in enumerate(soup.find_all("h2"), 1):
        print(f"{i}. {title.get_text(strip=True)}")

if __name__ == "__main__":
    url = input("Enter website URL: ")
    scrape_titles(url)
