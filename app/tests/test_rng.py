from pytest import fixture

from classes import RandomNumberGenerator


@fixture()
def rng_default():
    rng_default = RandomNumberGenerator(1, 90)
    return rng_default


@fixture()
def rng_with_count():
    rng_with_count = RandomNumberGenerator(1, 90, 15)
    return rng_with_count


class TestRandomNumberGenerator:

    def test_init_default(self, rng_default):
        assert len(rng_default.numbers) == 90
        for keg_number in range(1, 90 + 1):
            assert keg_number in rng_default.numbers

    def test_init_with_count(self, rng_with_count):
        assert len(rng_with_count.numbers) == 15

    def test_pop_random_number(self, rng_default):
        keg_number = rng_default.pop_random_number()
        assert keg_number not in rng_default.numbers
        assert len(rng_default.numbers) == 89

    def test_generator_is_empty(self, rng_default):
        for counter in range(1, 90 + 1):
            keg_number = rng_default.pop_random_number()
        # No more numbers
        keg_number = rng_default.pop_random_number()
        assert keg_number is None
