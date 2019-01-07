import unittest
from copy import deepcopy

from cards.card import Card
from cards.deck import Deck


class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_has_52_cards(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_shuffle(self):
        cards_copy = deepcopy(self.deck.cards)
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, cards_copy)

    def test_deal_card(self):
        card = self.deck.deal_card()
        self.assertEqual(len(self.deck.cards), 51)
        self.assertEqual(isinstance(card, Card), True)

    def test_deal_when_deck_is_empty(self):
        self.deck.cards.clear()
        card = self.deck.deal_card()
        self.assertEqual(card, None)

    def test_put_card_on_the_bottom(self):
        card = Card('test', 20)
        self.deck.put_card_on_bottom(card)
        self.assertEqual(
            self.deck.cards.index(card), 0
        )

    def test_put_multiple_cards_on_the_bottom(self):
        cards = [
            Card(suit, value) for suit, value in zip(
                ['Test', 'Test'], [1, 2]
            )
        ]
        self.deck.put_card_on_bottom(cards)
        self.assertEqual(self.deck.cards.popleft(), cards[1])
        self.assertEqual(self.deck.cards.popleft(), cards[0])


if __name__ == '__main__':
    unittest.main()
