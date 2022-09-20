from random import randint
from game_exceptions import EnemyDown
from game_exceptions import GameOver
from settings import LIVES, ALLOWED_ATTACKS



class Enemy():
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self, player_obj):
        self.lives -= 1
        if self.lives == 0:
            player_obj.scores += 5
            raise EnemyDown()

class Player():
    def __init__(self, name):
        self.name = name
        self.lives = LIVES
        self.score = 0
        self.allowed_attacks = ALLOWED_ATTACKS

    @staticmethod
    def fight(attack, defense):
        if attack < defense:
            return 1
        elif attack > defense or attack == 3 and defense == 1:
            return -1
        elif attack == defense:
            return 0

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print('\nYour score = ' + str(self.score) + '\n')
            GameOver.saveScore(self.score)
            raise GameOver()

    def attack(self, enemy_obj):
        print('\n\nEnemy HP = ' + str(enemy_obj.lives))
        print('Your HP = ' + str(self.lives) + '\n')
        print(self.name + ' attack!')
        player = int(input('Enter |1|-Sorcerer. |2|-Warrior. |3|-Robber: '))
        botNum = enemy_obj.select_attack()

        print('Your turn: ' + str(player))
        print('Enemy turn: ' + str(botNum))

        res = Player.fight(player, botNum)
        if res == 0:
            print("\nIt's a draw!\n")
        elif res == 1:
            print("\nYou attacked successfully!\n")
            self.score += 1
            enemy_obj.decrease_lives(self)
        else:
            print("\nYou missed!\n")

    def defence(self, enemy_obj):
        print('\n\nEnemy HP = ' + str(enemy_obj.lives))
        print('Your HP = ' + str(self.lives) + '\n')
        print(self.name + ', defend yourself!')
        player = int(input('Enter |1|-Sorcerer. |2|-Warrior. |3|-Robber: '))
        botNum = enemy_obj.select_attack()

        print('Your turn: ' + str(player))
        print('Enemy turn: ' + str(botNum))

        res = Player.fight(botNum, player)
        if res == 0:
            print("It's a draw!")
        elif res == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        else:
            print("Enemy missed!")