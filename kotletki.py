# -*- coding: utf-8 -*-

class Kotletka(object):
    ready_after = 2
    recommended_turns = 3
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
        return self._times_turned >= self.ready_after


class ChickenKotletka(Kotletka):
    ready_after = 4
    recommended_turns = 4


class ImpossibleKotletka(Kotletka):
    ready_after = 8
    recommended_turns = 8


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


class Burger(object):
    def __init__(self, kotletka, buns, sauce):
        if not kotletka.ready:
            raise KotletkaNotReadyException
        self.content = [buns[0], kotletka, sauce, buns[1]]
        self.ready = False
        self.i = 0
        self.bitting = ['OM', 'NOM',  'NOM',  'NOM']

    def wait(self):
        if self.ready:
            raise BurgerIsAlreadyReadyException
        else:
            self.ready = True

    def take_a_bite(self):
        return self.bitting.pop(0)

    def __iter__(self):
        return self

    def next(self):
        if not self.ready:
            raise BurgerIsNotReadyYetException
        if self.i > len(self.bitting):
            raise StopIteration
        else:
            self.i += 1
            return self.bitting.pop(0)

    @property
    def status(self):
        if len(self.bitting) == 4:
            if self.ready:
                return 'ready'
            else:
                return 'not ready'
        elif self.bitting:
            return 'not finished'
        else:
            return 'eaten'


class Cook(object):
    def __init__(self, cookbook):
        pass


class Cookbook(object):
    def __init__(self, recipes=[]):
        pass


class Recipe(object):
    def __init__(self):
        pass


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

class BurgerIsAlreadyReadyException(Exception):
    def __str__(self):
        return 'Your burger is ready already, Bon Appètit'

class BurgerIsNotReadyYetException(Exception):
    def __str__(self):
        return 'Burger wasn\'t cooked properly'


def order_burger():
    kokleta = Kotletka()
    while not kokleta.ready:
        kokleta.turn_over()
        return Burger(kokleta, [Bun(), Bun()], Ketchup())
