import math

NO_OF_CHECKS = 4   # ile razy sprawdzic
POSITION_MARGIN = 2   # jakie moze byc wahanie reki przy sprawdzaniu czy to ta sama pozycja


class Pozycjoner(object):
    def __init__(self, initial_pos):
        self.counter = 0
        self.last_pos = 0
        self.stable_pos = initial_pos

    def get_pos(self, pos):
        if self.is_stable(pos):
            # pozycja stabilna - uzyj tej nowej pozycji
            print "stabilna pozycja - mozna zmienic na nia"
            self.stable_pos = pos

        return self.stable_pos

    def is_stable(self, pos):
        diff = math.abs(self.last_pos - pos)
        self.last_pos = pos
        if diff <= POSITION_MARGIN:
            self.counter += 1
        else:
            self.counter = 0

        return self.counter >= NO_OF_CHECKS
