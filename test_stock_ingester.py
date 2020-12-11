from pprint import pprint
from unittest import TestCase
import stock_displayer as sd
import stock_ingester as si


class TestStockIngester(TestCase):
    def test_get_last_days(self):
        ingester = si.StockIngester()
        result = ingester.get_last_days("AAPL", "2020-11-04", "2020-11-10")
        pprint(result)

        displayer = sd.StockDisplayer()
        displayer.display_days("AAPL", result)

