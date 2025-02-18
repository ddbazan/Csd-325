#test_citites.py   
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        formatted_string = city_country("TOKYO", "JAPAN")
        self.assertEqual(formatted_string, "TOKYO, JAPAN")
if __name__ == '__main__':
     unittest.main()