class Kotletka(object):
    def __init__(self):
        self.up = True

    def turn_over(self):
        self.up = not self.up
