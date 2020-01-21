# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string

class Game:
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for x in range(9)]

    def is_valid(self, word):
        if len(word) > 0:
            result = True
            for letter in word:
                if letter not in self.grid:
                    result = False
                    break
            return result

        return False
