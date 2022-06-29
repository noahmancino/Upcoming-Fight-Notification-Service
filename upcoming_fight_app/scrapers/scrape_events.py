import re

from bs4 import BeautifulSoup
import requests

sherdog_address = "https://www.sherdog.com"


def scrape_upcoming_events():
    upcoming_events_path = "/organizations/Ultimate-Fighting-Championship-UFC-2"
    page_text = requests.get(sherdog_address + upcoming_events_path).text
    soup = BeautifulSoup(page_text, "html.parser")
    upcoming_events = soup.find_all("table")[0]
    rows = upcoming_events.select('tr[itemType="http://schema.org/Event"]')
    event_paths = [row.find("a")['href'] for row in rows]
    for event_path in event_paths:
        scrape_upcoming_event(sherdog_address + event_path)


def scrape_upcoming_event(event_url):
    page_text = requests.get(event_url).text
    soup = BeautifulSoup(page_text, "html.parser")
    date = soup.find("meta", {"itemprop": "startDate"})['content']
    name = soup.find("span", {"itemprop": "name"}).text
    print(f'name {name} date {date}')
    print('-' * 50)
    print('\n\n')
    fighter_urls = soup.find_all("a", {"itemprop": "url"})[1:]
    fighter_info = []
    for fighter_url in fighter_urls:
        scrape_fighter(fighter_url['href'])


def scrape_fighter(fighter_url):
    fighter_url = sherdog_address + fighter_url
    page_text = requests.get(fighter_url).text
    soup = BeautifulSoup(page_text, "html.parser")
    name = soup.find("span", {"class": "fn"}).text
    birth_date = soup.find("span", {"itemprop": "birthDate"}).string
    birth_date = re.findall('\d{4}', birth_date)[0]
    print(f'name {name} birth_date {birth_date}')


scrape_upcoming_events()
