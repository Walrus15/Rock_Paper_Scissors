import sys

from game_exceptions import GameOver
from models import Player
from models import Enemy


def play():
    lvl = 1
    enemyLives = 2


    name = input('Enter your nick: ')



    player = Player(name)
    enemy = Enemy(lvl, enemyLives)

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except:
            lvl += 1
            enemyLives += 2
            enemy = Enemy(lvl, enemyLives)




if __name__ == "__main__":
    menu = ''
    while True:

        print('Enter "start" to start the game.')
        print('Enter "scores" to show scores.')
        print('Enter "help" to show list commands.')
        print('Enter "exit" to exit the game.')

        try:
            menu = str(input('\nEnter: '))
        except:
            print('Input incorrect!')
        else:
            if menu == 'start':
                try:
                    play()
                except GameOver:
                    print('Game over!!!')
                except KeyboardInterrupt:
                    pass
                finally:
                    print('Good bye!')
            elif menu == 'scores':
                with open('scores.txt', 'a+') as file:
                    line = file.read()
                    print(line)

            elif menu == 'help':
                with open('requiremqnts.txt', 'a+') as file:
                    line = file.read()
                    print(line)
            elif menu == 'exit':
                print('Are you sure you want to exit the game?')
                yn = input('yes/no: ')
                if yn == 'yes':
                    sys.exit()
                if yn == 'no':
                    pass
