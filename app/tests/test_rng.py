from pytest import fixture, mark

from classes import RandomNumberGenerator


@fixture()
def rng():
    return RandomNumberGenerator(1, 90)


class TestRandomNumberGenerator:
    @mark.parametrize('min_number,max_number,count,expected_count',
                      [(1, 90, None, 90), (1, 90, 15, 15)])
    def test_init(self, min_number, max_number, count, expected_count):
        rng = RandomNumberGenerator(min_number, max_number, count)
        assert len(rng.numbers) == expected_count
        assert len(rng.numbers) == len(set(rng.numbers))

    def test_range_of_numbers(self, rng):
        for keg_number in range(1, 90 + 1):
            assert keg_number in rng.numbers
        assert 0 not in rng.numbers
        assert 91 not in rng.numbers

    def test_pop_random_number(self, rng):
        keg_number = rng.pop_random_number()
        assert keg_number not in rng.numbers
        assert len(rng.numbers) == 89

    def test_generator_is_empty(self, rng):
        for counter in range(1, 90 + 1):
            keg_number = rng.pop_random_number()
        # No more numbers
        keg_number = rng.pop_random_number()
        assert keg_number is None
