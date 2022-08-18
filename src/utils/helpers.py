import asyncio
import decimal
import functools


def normalize_fraction(value: decimal.Decimal) -> decimal.Decimal:
    normalized = value.normalize()
    sign, digits, exponent = normalized.as_tuple()
    if exponent > 0:
        return decimal.Decimal((sign, digits + (0,) * exponent, 0))
    else:
        return normalized


def format_price(value):
    return format(value, ',f')


def format_capitalization(value):
    return format(int(value), ',d')


def sync(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.get_event_loop().run_until_complete(f(*args, **kwargs))

    return wrapper
