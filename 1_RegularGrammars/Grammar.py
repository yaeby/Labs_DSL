import random

class Grammar:
    def __init__(self, V_n, V_t, P) :
        self.V_n = V_n
        self.V_t = V_t
        self.P = P

    def generate_string(self, word="S"):
        while (not self.check_word(word)):
            for char in word:
                if not self.check_symbol(char):
                    production = self.replace(
                        self.P[char])
                    word = word.replace(char, production)
        return word

    def check_word(self, word):
        for char in word:
            if char in self.V_n:
                return False
        return True

    def check_symbol(self, char):
        if char in self.V_n:
            return False
        return True

    def replace(self, P):
        return random.choice(P)