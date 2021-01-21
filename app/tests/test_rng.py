from pytest import fixture

from classes import RandomNumberGenerator


@fixture()
def rng():
    rng = RandomNumberGenerator(1, 90)
    return rng


class TestRandomNumberGenerator:

    def test_init(self, rng):
        assert len(rng.numbers) == 90
        for keg_number in range(1, 90 + 1):
            assert keg_number in rng.numbers

    def test_pop_random_number(self, rng):
        keg_number = rng.pop_random_number()
        assert keg_number not in rng.numbers
