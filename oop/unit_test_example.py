import unittest


class Currency:
    #exchange_rate: int

    def __init__(self, currency_code, exchange_rate):
        self.currency_code = currency_code
        self.exchange_rate = exchange_rate
        self.amount = 0.00

    def set_amount(self, amount):
        self.amount = amount

    def convert_to_usd(self):
        return self.amount * self.exchange_rate

    def convert_usd_to_currency(self, amount=None):
        to_convert = amount or self.amount
        return float(to_convert) / float(self.exchange_rate)

    def __gt__(self, other):
        return self.convert_to_usd() > other.convert_to_usd()

    def __eq__(self, other):
        return self.convert_to_usd() == other.convert_to_usd()

    def __lt__(self, other):
        return self.convert_to_usd() < other.convert_to_usd()

    def __le__(self, other):
        # less than equal to
        return self.convert_to_usd() <= other.convert_to_usd()

    def __ge__(self, other):
        # greater than equal to
        return self.convert_to_usd() >= other.convert_to_usd()

    def __repr__(self):
        return '<{},{},{}>'.format(self.currency_code, self.exchange_rate, self.amount)


class CurrencyTest(unittest.TestCase):
    """
    Please note never to name your test file as unittest.py as this will throw an error
    Python has a unittest.py file that it has to import and by naming your file as
    unittest.py, your file test imported instead.
    """

    def test_create_currency(self):
        pounds = Currency('GBP', 1.20)

        self.assertEqual(pounds.currency_code, 'GBP')
        self.assertEqual(pounds.exchange_rate, 1.20)

    def test_set_amount(self):
        pounds = Currency('GBP', 1.20)
        euros = Currency('EUR', 1.07)

        pounds.set_amount(5000)
        euros.set_amount(200)

        self.assertEqual(pounds.amount, 5000)
        self.assertEqual(euros.amount, 200)

    def test_compare_currency(self):
        pounds = Currency('GBP', 1.20)
        euros = Currency('EUR', 1.07)

        pounds.set_amount(200)
        euros.set_amount(200)

        self.assertTrue(pounds > euros)
        self.assertFalse(euros > pounds)
        self.assertFalse(pounds == euros)

    def test_comparison_with_exceptions(self):
        """
        To test that a correct type of exception will be thrown in our code
        """
        pounds = Currency('GBP', 1.20)
        pounds.set_amount(200)

        with self.assertRaises(AttributeError):
            pounds == 1000

    # if your code is not testable then it you should redesign your code
    # the methods in the code must be small and testable