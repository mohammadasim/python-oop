class Currency:
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


def __get_currency_resource(resource, transform=(lambda x: x)):
    """
    The transform parameter is just a place holder
    We can replace it with any lambda function that we want
    """
    data = {
        'items': [
            {'code': 'usd', 'amount_to_usd': 1.00},
            {'code': 'gbp', 'amount_to_usd': 1.21},
            {'code': 'eur', 'amount_to_usd': 1.07},
            {'code': 'jpy', 'amount_to_usd': 0.14},
            {'code': 'afg', 'amount_to_usd': 0.0125}

        ]
    }
    my_resource = data[resource]
    return [transform(x) for x in my_resource]


def get_currency_codes():
    return __get_currency_resource('items', lambda x: x['code'].upper())


print(get_currency_codes())


def get_currencies():
    return __get_currency_resource('items', lambda x: Currency(x['code'], x['amount_to_usd']))


print(get_currencies())

