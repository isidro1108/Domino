class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = []

    def take_tokens(self, table):
        for n in range(7):
            self.tokens.append(table.tokens.pop())
