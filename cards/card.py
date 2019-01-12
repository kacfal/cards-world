
class BaseCard:

    def __init__(self, suit, value):
        self.suit: str = suit
        self.value: int = value

    @property
    def display_name(self) -> str:
        return f'{self.value} of {self.suit.capitalize()}'

    def __str__(self) -> str:
        return self.display_name

    def __repr__(self) -> str:
        return self.display_name


class Card(BaseCard):
    def __init__(self, suit, value):
        super().__init__(suit, value)
        self.faces: dict = {
            11: 'Jack',
            12: 'Quin',
            13: 'King',
            14: 'Ace'
        }

    @property
    def display_name(self) -> str:
        display_value = self.faces.get(self.value, self.value)
        return f'{display_value} of {self.suit.capitalize()}'
