import random

class Grammar:
    def __init__(self, V_n, V_t, P) :
        self.V_n = V_n
        self.V_t = V_t
        self.P = P

    def generate_string(self, word="S"):
        while (not self.word_is_terminal(word)):
            for char in word:
                if not self.char_is_terminal(char):
                    production = self.__pick_replacement(
                        self.P[char])
                    word = word.replace(char, production)
        return word

    def word_is_terminal(self, word):
        for char in word:
            if char in self.V_n:
                return False
        return True

    def char_is_terminal(self, char):
        if char in self.V_n:
            return False
        return True

    def __pick_replacement(self, P):
        return random.choice(P)