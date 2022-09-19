


class GameOver(Exception):
    def __init__(self):
        pass

    @staticmethod
    def saveScore(player_obj):
        with open('scores.txt', 'a+') as fp:
            fp.write(player_obj.name + ' |' + player_obj.scores + '| ' + '\n')

class EnemyDown(Exception):
    def __init__(self):
        pass