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
            tokens_in_table+= '[{}{}]'.format(token.values[0], token.values[1])
        p_down = self.players[0].name
        p_top = self.players[1].name if len(self.players) == 2 else self.players[2].name
        p_right = '' if len(self.players) == 2 else 2 * ' ' + self.players[1].name
        p_left = 6 * ' ' if len(self.players) < 4 else self.players[3].name + (6 - len(self.players[3].name)) * ' '

        fill = 6 * ' ' + '|' + 112 * ' ' + '|'
        fill_for_tokens = (56 - (len(tokens_in_table)//2)) * ' '
        table = [7 * ' ' + 112 * '_', fill, fill, 
                p_left + '|' + fill_for_tokens + tokens_in_table + fill_for_tokens + '|' + p_right,
                fill, fill, 7 * ' ' + 112 * chr(175) + '\n']
        print((60 - len(p_top)//2) * ' ' + p_top)
        for line in table:
            print(line)
        tokens = ''
        for token in self.players[0].tokens:
            tokens+= '[{}{}] '.format(token.values[0], token.values[1])
        tokens_aside = ''
        for token in self.table.tokens_aside:
            tokens_aside+= '[||] '
        print((60 - len(p_down)//2) * ' ' + p_down)
        print((60 - len(tokens)//2) * ' ' + tokens)
        print('\nTokens aside: ' + tokens_aside)

game = Game()
game.display_welcome()
game.set_players()
game.set_game()
game.draw_table()
