from decimal import Decimal


class HourTooLowError(Exception):
    pass


class HourTooHighError(Exception):
    pass


rates = {
    'Chico': Decimal('0.5'),
    'Groucho': Decimal('0.7'),
    'Harpo': Decimal('0.5'),
    'Zeppo': Decimal('0.4')
}


def time_percentage(hour):
    return hour / Decimal('24.0')


def calculate_tax(price, region, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')
    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')

    return price + (price * rates[region] * time_percentage(hour))
