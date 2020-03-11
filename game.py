from table import *
from player import Player, CPU
from os import system
from time import sleep

class Game:
    def __init__(self):
        self.table = Table()
        self.players = []
        self.finish = False

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
        p = 1
        while len(self.players) != int(n_players):
            if self.table.message != '':
                print(self.table.message)
            name = input('Insert the name of the player: ')
            self.table.message = ''
            if len(name) > 1 and len(name) < 7:
                if p == 1:
                    self.players.append(Player(name))
                else:
                    self.players.append(CPU(name))
            else:
                self.table.message = "The player's name must have more than 1 character and less than 7\n"
            p+= 1
    
    def set_game(self):
        table = self.table
        table.create_tokens()
        table.shuffle_tokens()
        for player in self.players:
            player.take_tokens(table)
        if table.tokens:
            table.tokens_aside, table.tokens = table.tokens, table.tokens_aside

    def check_inputs(self, player, index, direction):
        max_index = len(player.tokens)
        well_index = index >= 0 and index < max_index
        well_direction = direction == 'r' or direction == 'l'
        return well_index and well_direction

    def check_number_input(self, index):
        if len(index) == 1:
            return ord(index) >= ord('0') and ord(index) <= ord('9')
        return False

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
        fill_for_tokens2 = (70 - (len(tokens_in_table)//2)) * ' ' if len(tokens_in_table) % 2 == 0 else ((70 - (len(tokens_in_table)//2)) - 1) * ' '
        table = [7 * ' ' + 140 * '_', fill, fill, 
                p_left + '|' + fill_for_tokens + tokens_in_table + fill_for_tokens2 + '|' + p_right,
                fill, fill, 7 * ' ' + 140 * chr(175) + '\n']
        self.draw_welcome()
        print('\nPlayer log:\n')
        print('{}    {}    {}'.format('Name','tokens','in step\n'))
        for player in self.players:
            n_spaces = 6 - len(player.name)
            print('{}{}     {}       {}'.format(player.name, n_spaces * ' ', len(player.tokens), player.in_step))
        print((74 - len(p_top)//2) * ' ' + p_top)
        for line in table:
            print(line)
        tokens = ''
        for token in self.players[0].tokens:
            tokens+= '[{}|{}] '.format(token.values[0], token.values[1])
        tokens_aside = ''
        for token in self.table.tokens_aside:
            tokens_aside+= '[|||] '
        indexes, i = '', 0
        for token in self.players[0].tokens:
            indexes+= '  {}   '.format(i)
            i+= 1
        print((74 - len(p_down)//2) * ' ' + p_down)
        print((74 - len(tokens)//2) * ' ' + tokens)
        print((74 - len(indexes)//2) * ' ' + indexes)
        print('\nTokens aside: ' + tokens_aside)
    
    def start(self):
        while True:
            for player in self.players:
                self.draw_table()
                if self.table.tokens_aside:
                    if not player.can_play(self.table) and player.tokens:
                        while not player.can_play(self.table) and self.table.tokens_aside:
                            player.take_token_from_aside(self.table)
                            self.draw_table()
                            sleep(1)
                if player.can_play(self.table):
                    if not isinstance(player, CPU):
                        while True:
                            self.draw_table()
                            index = input('\nCon cuál ficha quiere jugar?\n')
                            if self.table.tokens:
                                direction = input('En qué dirección quieres jugar?\n')
                            else:
                                direction = 'r'
                            if self.check_number_input(index):
                                index = int(index)
                                if self.check_inputs(player, index, direction):
                                    if player.play(self.table, index, direction):
                                        break
                    else:
                        player.play(self.table)
                        sleep(1)
                    if not player.tokens:
                        self.finish = True
                        break
                else:
                    player.in_step = 'step'
                    self.draw_table()
                    player.in_step = ''
                    sleep(1)
            if self.finish:
                break
        self.draw_table()
        print('\n' + player.name + ' you won!!!!!!\n')

game = Game()
game.display_welcome()
game.set_players()
game.set_game()
game.start()
