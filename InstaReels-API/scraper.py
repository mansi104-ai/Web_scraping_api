import requests
from bs4 import BeautifulSoup

class Scraper():
    def scrapedata(self, tag):
        url = f'https://www.instagram.com/reels{tag}/'
        r = requests.get(url)
        r.raise_for_status()

        # Create a Reel object
        soup = BeautifulSoup(r.text, 'html.parser')
        reel = soup.find('a', {'class': ''})

        if reel:  # Check if the element exists
            reel_link = reel['href']
            print(f"Downloaded reel link: {reel_link}")
        else:
            print("Reel link not found")

quotes = Scraper()
quotes.scrapedata('C2DHnJ1SL6T')