#!/usr/bin/env python3

from time import sleep

from classes import RandomNumberGenerator, Computer, Human

import config


def prepare_to_print(player_card):
    card = dict(zip(player_card.positions, player_card.numbers))
    card_to_print = []
    for i in range(0, config.FIELD_SIZE):
        if i in card:
            if card[i] in player_card.crossed_numbers:
                card_to_print.append('XX')
            elif card[i] >= 10:
                card_to_print.append(str(card[i]))
            else:
                card_to_print.append(f' {str(card[i])}')
        else:
            card_to_print.append('  ')
    return card_to_print


def print_card(player_card):
    card_to_print = prepare_to_print(player_card)
    # line size = field width * (2 characters per number + space) + borders
    line_size = config.FIELD_WIDTH * 3 + 3
    print("-" * line_size)
    first = 0
    for last in range(
            config.FIELD_WIDTH,
            config.FIELD_SIZE + 1,
            config.FIELD_WIDTH):
        row = ' '.join(card_to_print[first:last])
        print('|', f"{row}", '|')
        first = last
    print("-" * line_size)


class Game:
    def __init__(self):
        self.randoms = RandomNumberGenerator(1, 90)
        self.players = []
        self.step = 0
        self.keg = None
        self.winner = None

    def get_option(self):
        print(config.GREETING)
        try:
            option = int(input())
            if option not in range(0, config.MAX_PLAYERS + 1):
                option = None
        except ValueError:
            option = None
        return option

    def add_players(self, option):
        # @TODO - Improve this part
        self.players.append(Computer(config.NAMES[0]))
        if option == 0:
            self.players.append(Computer(config.NAMES[1]))
            return
        for i in range(1, option + 1):
            self.players.append(Human(config.NAMES[i]))

    def check_winner(self, players, player):
        if len(players) == 1:
            self.winner = players[0]
            return
        if player.is_winner:
            self.winner = player

    def play(self, option):
        self.add_players(option)
        while not self.winner:
            self.step += 1
            self.keg = self.randoms.pop_random_number()
            print(self)
            players = self.players.copy()
            for player in self.players:
                print(player)
                print_card(player.card)
                player.cross_number(self.keg)
                if player.is_looser:
                    print(f'{player} проиграл.')
                    players.remove(player)
                self.check_winner(players, player)
            self.players = players.copy()
            sleep(config.SLEEP_BETWEEN_MOVES)
        print(f'Победитель: {self.winner}.')
        print(f'В мешке остались бочонки: {self.randoms}.')

    def __str__(self):
        return f'Ход #{self.step}, Бочонок #{self.keg}'


def main():
    game = Game()
    option = game.get_option()
    if option is None:
        print('До свидания!')
        exit()
    game.play(option)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Игра прервана пользователем.')
