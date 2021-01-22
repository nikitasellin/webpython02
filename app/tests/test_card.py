from pytest import fixture

from classes import Card
import config


@fixture()
def card():
    return Card()


class TestCard:
    def test_init(self, card):
        assert len(card.numbers) == config.KEGS_PER_CARD
        assert len(card.positions) == config.KEGS_PER_CARD
        assert len(card.crossed_numbers) == 0
        assert len(card.numbers) == len(set(card.numbers))
        assert len(card.positions) == len(set(card.positions))

    def test_sub(self, card):
        number = card.numbers[0]
        assert number not in card.crossed_numbers
        card = card - number
        assert number in card.crossed_numbers
        assert number in card.numbers
