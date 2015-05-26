class Kotletka(object):
    ready_after = 2
    burnt_after = 5

    def __init__(self):
        self.up = True
        self._times_turned = 0

    def turn_over(self):
        self.up = not self.up
        self._times_turned += 1

        if self._times_turned >= self.burnt_after:
            raise KotletkaBurntException()

    @property
    def ready(self):
        return self._times_turned >= 2


class ChickenKotletka(Kotletka):
    ready_after = 4


class ImpossibleKotletka(Kotletka):
    ready_after = 8
    # burnt_after == 5


class Bun(object): pass


class Sauce(object): pass


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
            raise KotletkaNotReadyException
        self.extend([buns[0], kotletka, sauce, buns[1]])


class SkovorodaOverflowException(Exception):
    def __str__(self):
        return 'Too many items at skovoroda'


class YouSuckAtCookingException(Exception):
    def __str__(self):
        return 'Your chef sucks at cooking'


class KotletkaBurntException(YouSuckAtCookingException):
    def __str__(self):
        return 'Kotletka was overcooked'


class KotletkaNotReadyException(YouSuckAtCookingException):
    def __str__(self):
        return "Kotletka wasn't cooked properly"
