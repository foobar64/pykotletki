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


class Bun(object):
    def __init__(self):
        pass


class Sauce(object):
    def __init__(self):
        pass


class Ketchup(Sauce):
    def __init__(self):
        Sauce.__init__(self)
        self.color = 'red'


class Skovoroda(object):
    def __init__(self):
        self.contents = []

    def put(self, food):
        if len(self.contents) > 5:
            raise SkovorodaOverflowException
        self.contents.append(food)


class Burger(list):
    def __init__(self, kotletka, buns, sauce):
        if not kotletka.ready:
            raise YouSuckAtCookingException
        self.extend([buns[0], kotletka, sauce, buns[1]])


class SkovorodaOverflowException(Exception):
    def __str__(self):
        return 'Wow such exception'


class YouSuckAtCookingException(Exception):
    def __str__(self):
        return 'Your chef sucks at cooking'
