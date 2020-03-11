from table import *
from player import Player
from os import system
from time import sleep

class Game:
    def __init__(self):
        self.table = Table()
        self.players = []

    def draw_welcome(self):
        print('\n\n' + 71 * '*' + 11 * ' ' + 71 * '*')
        print(71 * '*' + 'Domino Game' + 71 * '*')
        print(71 * '*' + 11 * ' ' + 71 * '*' + '\n')

    def display_welcome(self):
        bar = 15 * ' '
        for n in range(15):
            system('cls')
            bar = bar[:n] + '|' + bar[n + 1:]
            self.draw_welcome()
            print(68 * ' ' + '[' + bar + ']')
            print(75 * ' ' + '{}%'.format(round(n/15 * 100)))
            sleep(random())

    def set_players(self):
        system('cls')
        print('\nmin: 2 players | max: 4 players')
        n_players = input('\nHow many players will have in the game?\n')
        if n_players not in '234' or len(n_players) != 1:
            return self.set_players()
        while len(self.players) != int(n_players):
            if self.table.message != '':
                print(self.table.message)
            name = input('Insert the name of the player: ')
            self.table.message = ''
            if len(name) > 1 and len(name) < 7:
                self.players.append(Player(name))
            else:
                self.table.message = "The player's name must have more than 1 character and less than 7\n"
    
    def set_game(self):
        table = self.table
        table.create_tokens()
        table.shuffle_tokens()
        for player in self.players:
            player.take_tokens(table)
        if table.tokens:
            table.tokens_aside, table.tokens = table.tokens, table.tokens_aside

    def draw_table(self):
        system('cls')
        tokens_in_table = ''
        for token in self.table.tokens:
            tokens_in_table+= '[{}|{}]'.format(token.values[0], token.values[1])
        p_down = self.players[0].name
        p_top = self.players[1].name if len(self.players) == 2 else self.players[2].name
        p_right = '' if len(self.players) == 2 else (6 - len(self.players[1].name)) * ' ' + self.players[1].name
        p_left = 6 * ' ' if len(self.players) < 4 else self.players[3].name + (6 - len(self.players[3].name)) * ' '

        fill = 6 * ' ' + '|' + 140 * ' ' + '|'
        fill_for_tokens = (70 - (len(tokens_in_table)//2)) * ' '
        table = [7 * ' ' + 140 * '_', fill, fill, 
                p_left + '|' + fill_for_tokens + tokens_in_table + fill_for_tokens + '|' + p_right,
                fill, fill, 7 * ' ' + 140 * chr(175) + '\n']
        self.draw_welcome()
        print((74 - len(p_top)//2) * ' ' + p_top)
        for line in table:
            print(line)
        tokens = ''
        for token in self.players[0].tokens:
            tokens+= '[{}|{}] '.format(token.values[0], token.values[1])
        tokens_aside = ''
        for token in self.table.tokens_aside:
            tokens_aside+= '[|||] '
        print((74 - len(p_down)//2) * ' ' + p_down)
        print((74 - len(tokens)//2) * ' ' + tokens)
        print('\nTokens aside: ' + tokens_aside)

# game = Game()
# game.display_welcome()
# game.set_players()
# game.set_game()
# game.draw_table()
table = Table()
table.create_tokens()
table.shuffle_tokens()
player1 = Player('yo')
player1.take_tokens(table)
table.tokens = []
# for n in range(4):
#     player1.take_tokens(table)

while True:
    system('cls')
    tokens_in_table = ''
    for token in table.tokens:
        tokens_in_table+= '[{}|{}]'.format(token.values[0], token.values[1])
    tokens = ''
    for token in player1.tokens:
        tokens+= '[{}|{}] '.format(token.values[0], token.values[1])
    print('\n' + tokens_in_table + '\n')
    print(tokens)
    if not player1.can_play(table):
        break
    index = int(input('\nCon cuál ficha quiere jugar?\n'))
    direction = input('En qué dirección quieres jugar?\n')
    player1.play(table, index, direction)
