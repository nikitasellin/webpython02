from pytest import mark, fixture

from lotto import Game


@fixture(scope='function')
def game():
    return Game()


class TestGame:
    @mark.parametrize('option,players_count,p_types',
                      [(0, 2, ['Компьютер', 'Компьютер']),
                       (1, 2, ['Компьютер', 'Человек']),
                       (2, 3, ['Компьютер', 'Человек', 'Человек']),
                       (4, 5, ['Компьютер', 'Человек', 'Человек', 'Человек', 'Человек'])
                       ])
    def test_add_players(self, option, players_count, p_types, game):
        game.add_players(option)
        assert len(game.players) == players_count
        player_types = [player.p_type for player in game.players]
        assert player_types == p_types
