from collections import deque
from itertools import product
from random import shuffle
from typing import Optional, List

from cards.card import Card
from cards.configuration import SUITS, VALUES
from cards.utils import method_dispatch


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

    @method_dispatch
    def put_card_on_bottom(self, card) -> None:
        """
        Generic dispatch method which allows for different actions
        for different data types.
        :param card: Card instance or Iterable
        :return: None
        """
        raise NotImplementedError(
            'put_card_on_bottom accept Card instance or iterable of Card'
        )

    @put_card_on_bottom.register
    def _(self, card: Card) -> None:
        """
        Puts given card on the bottom of deque
        :param card: Card instance
        :return: None
        """

        self.cards.appendleft(card)

    @put_card_on_bottom.register
    def _(self, cards: list) -> None:
        """
        Puts given iterable of cards on the bottom of deque
        :param cards: Iterable[Card]
        :return: None
        """
        # FIXME this method should accept only list of Card (List[Card])

        self.cards.extendleft(cards)


deck = Deck(SUITS, VALUES)
