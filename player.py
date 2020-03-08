class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.tokens = []

    def take_tokens(self, table):
        for n in range(7):
            self.tokens.append(table.tokens.pop())
