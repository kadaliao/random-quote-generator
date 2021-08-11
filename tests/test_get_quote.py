from random_quote_generator import get_quote
from random_quote_generator.quotes import quotes


def test_get_quote():
    quote = get_quote()
    assert quote in quotes
