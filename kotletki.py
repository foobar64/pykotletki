class Kotletka(object):
    def __init__(self):
        self.up = True
        self._times_turned = 0

    def turn_over(self):
        self.up = not self.up
        self._times_turned += 1
    
    @property
    def ready(self):
        return self._times_turned >= 2
