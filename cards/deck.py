from collections import deque
from itertools import product
from random import shuffle
from typing import Iterable as IterableType, Iterable, Optional, List

from cards.card import Card
from cards.dictionary import SUITS, VALUES


class Deck:
    def __init__(self, suits: List[str], values: List[int]):
        self.cards = deque(
            [
                Card(suit, value) for suit, value in product(suits, values)
            ]
        )

    def __str__(self) -> str:
        return str(self.cards)

    def shuffle(self) -> None:
        """
        Shuffle deck of cards with random.shuffle() function
        :return: None
        """
        shuffle(self.cards)

    def deal_card(self) -> Optional[Card]:
        """
        Returns card from the top of the deck
        :return: Deck or None
        """
        try:
            return self.cards.pop()
        except IndexError:
            return None

    def put_card_on_bottom(self, card: [Card, IterableType]) -> None:
        """
        Puts given card or iterable of cards on the bottom of deque
        :param card: Card instance or Itarable
        :return: None
        """
        if isinstance(card, Iterable):
            self.cards.extendleft(card)
        else:
            self.cards.appendleft(card)


deck = Deck(SUITS, VALUES)
