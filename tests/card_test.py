import pytest

from cards.card import Card


@pytest.mark.parametrize("card,expected", [
    (Card('hearts', 2), "2 of Hearts"),
    (Card('hearts', 11), "Jack of Hearts"),
    (Card('hearts', 12), "Quin of Hearts"),
    (Card('hearts', 13), "King of Hearts"),
    (Card('hearts', 14), "Ace of Hearts")
])
def cards_names_test(card, expected):
    assert card.display_name == expected
    assert card.__str__() == expected
    assert card.__repr__() == expected
