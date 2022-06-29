from bs4 import BeautifulSoup
import requests

# This scraper assumes a lot about the structure of the wikipedia page that could easily change

fight_tables = ((9, 'Heavyweight'), (10, 'Light Heavyweight'), (11, 'Middleweight'), (12, 'Welterweight'),
                (13, 'Lightweight'), (14, 'Featherweight'), (15, 'Bantamweight'), (16, 'Flyweight'),
                (17, 'Women\'s Featherweight'), (18, 'Women\'s Bantamweight'), (19, 'Women\'s Flyweight'),
                (20, 'Women\'s Strawweight'))
list_of_fighters_url = "https://en.wikipedia.org/wiki/List_of_current_UFC_fighters"


def get_list_of_fighters():
    page_text = requests.get(list_of_fighters_url).text
    soup = BeautifulSoup(page_text, 'html.parser')
    tables = soup.find_all('table')
    for index, division in fight_tables:
        table = tables[index]
        rows = table.findChildren('tr')
        rows = [row for row in rows if len(row.findChildren('td')) == 9]
        for row in rows:
            cells = row.findChildren('td')
            print(
                f'name: {parse_span_cell(cells[1])}, age: {parse_span_cell(cells[2])}, nickname: {parse_nickname(cells[4])}')


def parse_span_cell(cell):  # TODO: get rid of asterisk and (C)
    if cell.text:
        return cell.text.strip()
    else:
        return cell.find("span", class_="data-sort-value").strip()


def parse_nickname(cell):
    nickname = cell.find('i')
    return nickname.text if nickname else ""
