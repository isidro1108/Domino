from table import *
from player import Player
from os import system
from time import sleep

class Game:
    def __init__(self):
        self.table = Table()
        self.players = []

    def display_welcome(self):
        bar = 15 * ' '
        for n in range(15):
            system('cls')
            bar = bar[:n] + '|' + bar[n + 1:]
            print('\n\n' + 20 * '*' + 11 * ' ' + 20 * '*')
            print(20 * '*' + 'Domino Game' + 20 * '*')
            print(20 * '*' + 11 * ' ' + 20 * '*' + '\n')
            print(17 * ' ' + '[' + bar + ']')
            print(24 * ' ' + '{}%'.format(round(n/15 * 100)))
            sleep(random())

    def set_players(self):
        system('cls')
        print('\nmin: 2 players | max: 4 players')
        n_players = input('\nHow many players will have in the game?\n')
        if n_players not in '234' or len(n_players) != 1:
            return self.set_players()
        for n in range(int(n_players)):
            name = input('Insert the name of the player: ')
            self.players.append(Player(name))
    
    def set_game(self):
        table = self.table
        table.create_tokens()
        table.shuffle_tokens()
        for player in self.players:
            player.take_tokens(table)
        if table.tokens:
            table.tokens_aside, table.tokens = table.tokens, table.tokens_aside

game = Game()
game.display_welcome()
game.set_players()
game.set_game()
for player in game.players:
    tokens = ''
    for token in player.tokens:
        tokens+= '[{}|{}] '.format(token.values[0], token.values[1])
    print(player.name, tokens)
    print()
tokens_aside = ''
for token in game.table.tokens_aside:
    tokens_aside+= '[{}|{}] '.format(token.values[0], token.values[1])
print('Tokens aside: ' + tokens_aside)
print(game.table.tokens)
