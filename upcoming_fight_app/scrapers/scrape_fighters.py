# from bs4 import BeautifulSoup
# import requests
# import re
# import unidecode
# from datetime import date
# from upcoming_fight_app.models import Fighter
#
# # This scraper assumes a lot about the structure of the wikipedia page that could easily change
#
# fight_tables = ((9, 'Heavyweight'), (10, 'Light Heavyweight'), (11, 'Middleweight'), (12, 'Welterweight'),
#                 (13, 'Lightweight'), (14, 'Featherweight'), (15, 'Bantamweight'), (16, 'Flyweight'),
#                 (17, 'Women\'s Featherweight'), (18, 'Women\'s Bantamweight'), (19, 'Women\'s Flyweight'),
#                 (20, 'Women\'s Strawweight'))
# list_of_fighters_url = "https://en.wikipedia.org/wiki/List_of_current_UFC_fighters"
#
#
# def get_list_of_fighters():
#     page_text = requests.get(list_of_fighters_url).text
#     soup = BeautifulSoup(page_text, 'html.parser')
#     tables = soup.find_all('table')
#     for index, division in fight_tables:
#         table = tables[index]
#         rows = table.findChildren('tr')
#         rows = [row for row in rows if len(row.findChildren('td')) == 9]
#         print(division)
#         for row in rows:
#             cells = row.findChildren('td')
#             fighter_name = unidecode.unidecode(cells[1].text)
#             fighter_name = re.sub(r'\(C\)', '', fighter_name) # Champions have (C) after their name
#             fighter_name = re.sub(r"[^a-z^ ^-^']", '', fighter_name, flags=re.IGNORECASE)
#             fighter_name = fighter_name.strip()
#             age = int(cells[2].text)
#             youngest_possible_birthday = date.today().year - age
#             oldest_possible_birthday = youngest_possible_birthday - 1
#             nickname = cells[4].text.strip()
#             if not Fighter.exists_by_name_and_birthdays(fighter_name, youngest_possible_birthday,
#                                                         oldest_possible_birthday):
#                 new_fighter = Fighter(name=fighter_name, youngest_possible_birthday=youngest_possible_birthday,
#                                       oldest_possible_birthday=oldest_possible_birthday, nickname=nickname,
#                                       weight_class=division)
#                 new_fighter.save()
#
#
# def parse_span_cell(cell):  # TODO: get rid of asterisk and (C)
#     if cell.text:
#         return cell.text.strip()
#
#
# def parse_nickname(cell):
#     nickname = cell.find('i')
#     return nickname.text if nickname else ""
