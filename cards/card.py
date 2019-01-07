
class Card:

    def __init__(self, suit, value):
        self.suit: str = suit
        self.value: int = value
        self.faces: dict = {
            11: 'jack',
            12: 'quin',
            13: 'king',
            14: 'ace'
        }

    def __str__(self) -> str:
        return f'{self.value} of {self.suit.capitalize()}'

    def __repr__(self) -> str:
        return f'{self.value} of {self.suit.capitalize()}'
