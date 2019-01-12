from typing import Optional, List

from cards.card import Card
from cards.deck import Deck, deck
from games.wargame.players import Player


class WarGame:

    def __init__(self, players: List[Player]) -> None:
        self.deck: Deck = deck
        self.players: List[Player] = players

    @classmethod
    def compare_cards(cls, card_1: Card, card_2: Card) -> Optional[Card]:
        """
        Returns card with bigger value
        Doesn't compare suits

        :param card_1: Card
        :param card_2: Card
        :return: Card or None
        """
        if card_1.value == card_2.value:
            return None
        return max(
            [card_1, card_2], key=lambda c: c.value
        )

    def deal_cards(self) -> None:
        """
        Deal all cards to players hands
        :return: None
        """
        self.deck.shuffle()
        while self.deck.cards:
            for player in self.players:
                player.cards.append(
                    self.deck.deal_card()
                )

    def start(self):
        pass
