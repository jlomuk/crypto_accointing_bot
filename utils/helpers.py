import decimal


def normalize_fraction(value: decimal.Decimal) -> decimal.Decimal:
    normalized = value.normalize()
    sign, digits, exponent = normalized.as_tuple()
    if exponent > 0:
        return decimal.Decimal((sign, digits + (0,) * exponent, 0))
    else:
        return normalized
