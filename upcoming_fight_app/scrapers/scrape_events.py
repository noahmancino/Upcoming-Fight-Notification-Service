import re
from bs4 import BeautifulSoup
import requests
from urllib.error import URLError
from upcoming_fight_app.models import Fighter

sherdog_address = "https://www.sherdog.com"

# TODO: send an email to myself if any error is logged, because sherdog probably changed in some way

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
    fighter_properties = {}
    fighter_url = sherdog_address + fighter_url
    fighter_properties["sherdog_url"] = fighter_url
    page_text = requests.get(fighter_url).text
    soup = BeautifulSoup(page_text, "html.parser")

    name = soup.find("span", {"class": "fn"}).text
    fighter_properties["name"] = name

    nickname = soup.find("span", {"class": "nickname"})
    nickname = nickname.text.strip("\"") if nickname is not None else ""
    fighter_properties["nickname"] = nickname

    birth_date = soup.find("span", {"itemprop": "birthDate"}).string
    birth_date = int(re.findall("\d{4}", birth_date)[0])
    fighter_properties["birth_date"] = birth_date

    weight = soup.find("b", {"itemprop": "weight"}).text
    weight = int(re.sub("[^0-9]", "", weight))
    fighter_properties["weight_class"] = weight

    new_fighter = Fighter(**fighter_properties)
    new_fighter.save()
