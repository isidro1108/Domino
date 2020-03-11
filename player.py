class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.tokens = []
        self.dirs = {'left': 0, 'right': -1}

    def take_tokens(self, table):
        for n in range(7):
            self.tokens.append(table.tokens.pop())

    def can_play(self, table):
        v1, v2 = table.tokens[0].values[0], table.tokens[-1].values[1]
        for token in self.tokens:
            for value in token.values:
                if value == v1 or value == v2:
                    return True
        return False
    
    def can_play_token(self, table, index, dir):
        token_in_table = table.tokens[self.dirs[dir]].values[self.dirs[dir] * -1]
        my_token = self.tokens[index]
        return token_in_table == my_token.values[0] or token_in_table == my_token.values[1]

    def play(self, table, index, dir):
        if not table.tokens:
            table.tokens.append(self.tokens.pop(index))
            return True
        if self.can_play_token(table, index, dir):
            token_in_table = table.tokens[self.dirs[dir]].values[self.dirs[dir] * -1]
            my_token = self.tokens[index].values[self.dirs[dir]]
            if my_token == token_in_table:
                self.tokens[index].values[0], self.tokens[index].values[1] = self.tokens[index].values[1], self.tokens[index].values[0]
                table.tokens.append(self.tokens.pop(index))
                return True
            else:
                table.tokens.append(self.tokens.pop(index))
                return True
        return False
