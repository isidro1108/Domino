from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.tokens = []
        self.directions = {'l': 0, 'r': -1}
        self.in_step = ''

    def take_tokens(self, table):
        for n in range(7):
            self.tokens.append(table.tokens.pop())
    
    def take_token_from_aside(self, table):
        self.tokens.append(table.tokens_aside.pop())

    def can_play(self, table):
        if table.tokens:
            v1, v2 = table.tokens[0].values[0], table.tokens[-1].values[1]
            for token in self.tokens:
                for value in token.values:
                    if value == v1 or value == v2:
                        return True
            return False
        return True
    
    def can_play_token(self, table, index, direction):
        token_in_table = table.tokens[self.directions[direction]].values[self.directions[direction] * -1]
        my_token = self.tokens[index]
        return token_in_table == my_token.values[0] or token_in_table == my_token.values[1]

    def put_token(self, table, index, direction):
        if direction == 'r':
            table.tokens.append(self.tokens.pop(index))
        elif direction == 'l':
            table.tokens = [self.tokens.pop(index)] + table.tokens

    def play(self, table, index, direction):
        if not table.tokens:
            table.tokens.append(self.tokens.pop(index))
            return True
        if self.can_play_token(table, index, direction):
            token_in_table = table.tokens[self.directions[direction]].values[self.directions[direction] * -1]
            my_token = self.tokens[index].values[self.directions[direction]]
            if my_token == token_in_table:
                self.tokens[index].values[0], self.tokens[index].values[1] = self.tokens[index].values[1], self.tokens[index].values[0]
                self.put_token(table, index, direction)
                return True
            else:
                self.put_token(table, index, direction)
                return True
        return False

class CPU(Player):
    def random_index(self, table):
        for index in range(len(self.tokens)):
            if self.can_play_token(table, index, 'l'):
                return index, 'l'
            elif self.can_play_token(table, index, 'r'):
                return index, 'r'

    def play(self, table):
        if not table.tokens:
            r_index = randint(0, len(self.tokens))
            table.tokens.append(self.tokens.pop(r_index))
            return True
        index, direction = self.random_index(table)
        token_in_table = table.tokens[self.directions[direction]].values[self.directions[direction] * -1]
        my_token = self.tokens[index].values[self.directions[direction]]
        if my_token == token_in_table:
            self.tokens[index].values[0], self.tokens[index].values[1] = self.tokens[index].values[1], self.tokens[index].values[0]
            self.put_token(table, index, direction)
            return True
        else:
            self.put_token(table, index, direction)
            return True
