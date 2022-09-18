


class GameOver(Exception):
    def __init__(self, scores):
        self.scores = scores


    def saveScore(self):
        with open('scores.txt', 'a+') as fp:
            fp.write(self.scores + '\n')

class EnemyDown(Exception):
    pass