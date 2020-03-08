from token import Token

class Table:
    def __init__(self):
        self.tokens = []

    def create_tokens(self):
        for v1 in range(7):
            for v2 in range(v1, 7):
                self.tokens.append(Token(v1, v2))
