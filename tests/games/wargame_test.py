import pytest

from cards.card import Card
from games.wargame.main import WarGame
from games.wargame.players import Player

card_1 = Card('A', 3)
card_2 = Card('B', 6)
card_3 = Card('B', 6)


@pytest.fixture()
def game():
    return WarGame([Player(), Player()])


@pytest.mark.parametrize("cards,expected", [
    ([card_1, card_2], card_2),
    ([card_1, card_1], None),
    ([card_3, card_3], None)
])
def compare_cards_test(cards, expected, game):
    bigger_card = game.compare_cards(*cards)

    assert bigger_card == expected


def deal_all_cards_test(game):
    amount_of_cards_per_player = len(game.deck.cards) / len(game.players)

    game.deal_cards()

    assert not game.deck.cards
    assert amount_of_cards_per_player == len(game.players[0].cards)
    assert amount_of_cards_per_player == len(game.players[1].cards)
