from collections import deque
from itertools import product
from random import shuffle
from typing import Iterable as IterableType, Iterable

from cards.card import Card


class Deck:
    def __init__(self):
        self.cards = deque(
            [
                Card(suit, value) for suit, value in product(SUITS, VALUES)
            ]
        )

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def deal_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            return None

    def put_card_on_bottom(self, card: [Card, IterableType]):
        """
        Puts given card or iterable of cards on the bottom of deque
        :param card: Card instance or Itarable
        :return: None
        """
        if isinstance(card, Iterable):
            self.cards.extendleft(card)
        else:
            self.cards.appendleft(card)


SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
VALUES = [*[num for num in range(2, 11)], *['jack', 'quin', 'king', 'ace']]
