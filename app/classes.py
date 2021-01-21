from random import shuffle

import config


class RandomNumberGenerator:
    def __init__(self, min_num, max_num, count=None):
        # Start from 1, not 0
        max_num = max_num + 1
        if not count:
            count = max_num - min_num
        num_list = list(range(min_num, max_num))
        shuffle(num_list)
        self._numbers = num_list[0: count]

    @property
    def numbers(self):
        return self._numbers

    def pop_random_number(self):
        try:
            return self._numbers.pop(0)
        except IndexError:
            return None

    def __str__(self):
        str_numbers = [str(el) for el in self._numbers]
        return ', '.join(str_numbers)


class Card:
    def __init__(self):
        self.numbers = []
        self.crossed_numbers = []
        self.positions = []
        all_numbers = RandomNumberGenerator(
            1, 90, config.KEGS_PER_CARD).numbers
        pos = 1
        nums = 1
        for i in range(0, config.FIELD_HEIGHT):
            line_positions = RandomNumberGenerator(
                pos, pos + config.FIELD_WIDTH, config.KEGS_PER_LINE).numbers
            line_positions.sort()
            self.positions.extend(line_positions)
            pos += config.FIELD_WIDTH
            line_numbers = all_numbers[nums:nums + config.KEGS_PER_LINE]
            line_numbers.sort()
            self.numbers.extend(line_numbers)
            nums += config.KEGS_PER_LINE

    def __sub__(self, number):
        if number not in self.numbers:
            raise ValueError(f'В карточке нет номера "{number}".')
        self.crossed_numbers.append(number)
        return self


class Player:
    p_type = None

    def __init__(self, p_name=None):
        self.p_name = p_name
        self.card = Card()
        self.is_looser = False
        self.is_winner = False

    def cross_number(self, number):
        raise NotImplementedError('Неправильный тип игрока!')

    @property
    def card_is_full(self):
        if len(self.card.crossed_numbers) == len(self.card.numbers):
            return True
        return False

    def __str__(self):
        return f'{self.p_name} ({self.p_type})'


class Human(Player):
    p_type = 'Человек'

    def cross_number(self, number):
        choice = self.get_choice()
        try:
            self.card = self.card - number
            crossed = True
        except ValueError:
            crossed = False
        if self.card_is_full:
            self.is_winner = True
            return
        if (crossed and choice == 'n') or (not crossed and choice == 'y'):
            print('Неверный выбор!')
            self.is_looser = True

    @staticmethod
    def get_choice():
        choice = input('Зачеркнуть (y/n)? ').lower()
        while choice not in ('y', 'n'):
            print('Неверный символ.')
            choice = input('Зачеркнуть (y/n)? ').lower()
        return choice


class Computer(Player):
    p_type = 'Компьютер'

    def cross_number(self, number):
        try:
            self.card = self.card - number
        except ValueError:
            pass
        finally:
            if self.card_is_full:
                self.is_winner = True
