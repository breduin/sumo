from dataclasses import dataclass


@dataclass
class BoutResults:
    WINNER = 'W'
    LOSER = 'L'

    @classmethod
    def get_opposite(cls, result):
        return cls.LOSER if result == cls.WINNER else cls.WINNER


@dataclass(frozen=True)
class Kakuzuke:
    MAKUSHITA = 3, 'Makushita'
    JURYO = 2, 'Juryo'
    MAKUUCHI = 1, 'Makuuchi'
