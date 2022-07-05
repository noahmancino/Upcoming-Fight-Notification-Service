from django.test import TestCase, SimpleTestCase
import upcoming_fight_app.scrapers.scrape_events as scrape_events


class TestScrapers(SimpleTestCase):
    def testScrapeFighterArmen(self):
        result_dict = scrape_events.scrape_fighter("/fighter/Armen-Petrosyan-302783")
        expected_dict = {"name": "Armen Petrosyan", "nickname": "Superman", "birth_date": 1990, "weight": 186,
                         "sherdog_url": "https://www.sherdog.com/fighter/Armen-Petrosyan-302783"}
        print(result_dict)
        self.assertEqual(expected_dict, result_dict)
