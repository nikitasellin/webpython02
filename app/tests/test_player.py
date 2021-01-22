from unittest import mock

from pytest import fixture

from classes import Computer, Human


@fixture(scope='function')
def computer():
    return Computer()


@fixture(scope='function')
def human():
    return Human()


class TestComputer:
    def test_computer_cross_existent_number(self, computer):
        max_number_in_card = max(computer.card.numbers)
        computer.cross_number(max_number_in_card)
        assert len(computer.card.crossed_numbers) == 1
        assert computer.card.crossed_numbers[0] == max_number_in_card
        assert computer.is_looser is False
        assert computer.is_winner is False

    def test_computer_cross_non_existent_number(self, computer):
        max_number_in_card = max(computer.card.numbers)
        computer.cross_number(max_number_in_card + 1)
        assert len(computer.card.crossed_numbers) == 0
        assert computer.is_looser is False
        assert computer.is_winner is False

    def test_computer_wins(self, computer):
        for number in computer.card.numbers:
            computer.cross_number(number)
        assert computer.is_looser is False
        assert computer.is_winner is True


class TestHuman:
    @mock.patch('classes.Human.get_choice', autospec=True)
    def test_human_cross_existent_number_right_choice(self, mocked_get_choice, human):
        max_number_in_card = max(human.card.numbers)
        mocked_get_choice.return_value = 'y'
        human.cross_number(max_number_in_card)
        assert len(human.card.crossed_numbers) == 1
        assert human.card.crossed_numbers[0] == max_number_in_card
        assert human.is_looser is False
        assert human.is_winner is False

    @mock.patch('classes.Human.get_choice', autospec=True)
    def test_human_cross_existent_number_wrong_choice(self, mocked_get_choice, human):
        max_number_in_card = max(human.card.numbers)
        mocked_get_choice.return_value = 'n'
        human.cross_number(max_number_in_card)
        assert len(human.card.crossed_numbers) == 1
        assert human.is_looser is True

    @mock.patch('classes.Human.get_choice', autospec=True)
    def test_human_cross_non_existent_number_right_choice(self, mocked_get_choice, human):
        max_number_in_card = max(human.card.numbers)
        mocked_get_choice.return_value = 'n'
        human.cross_number(max_number_in_card + 1)
        assert len(human.card.crossed_numbers) == 0
        assert human.is_looser is False

    @mock.patch('classes.Human.get_choice', autospec=True)
    def test_human_cross_non_existent_number_wrong_choice(self, mocked_get_choice, human):
        max_number_in_card = max(human.card.numbers)
        mocked_get_choice.return_value = 'y'
        human.cross_number(max_number_in_card + 1)
        assert len(human.card.crossed_numbers) == 0
        assert human.is_looser is True
        assert human.is_winner is False

    @mock.patch('classes.Human.get_choice', autospec=True)
    def test_human_wins(self, mocked_get_choice, human):
        mocked_get_choice.return_value = 'y'
        for number in human.card.numbers:
            human.cross_number(number)
        assert human.is_looser is False
        assert human.is_winner is True
