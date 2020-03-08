from token import Token
from random import randint

class Table:
    def __init__(self):
        self.tokens = []

    def create_tokens(self):
        for v1 in range(7):
            for v2 in range(v1, 7):
                self.tokens.append(Token(v1, v2))

    def shuffle_tokens(self):
        for n in range(len(self.tokens)):
            r = randint(0, len(self.tokens)-1)
            self.tokens[n], self.tokens[r] = self.tokens[r], self.tokens[n]
