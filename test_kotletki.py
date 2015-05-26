import itertools
import unittest
from kotletki import Kotletka, Bun, Sauce, Ketchup, Skovoroda, Burger
from kotletki import ChickenKotletka, ImpossibleKotletka
from kotletki import SkovorodaOverflowException, YouSuckAtCookingException


class TestSkovorodii(unittest.TestCase):
    def test_put_something(self):
        tefal = Skovoroda()
        tefal.put('salo')
        self.assertEqual(tefal.contents, ['salo'])

    def test_kuda_kladesh_stolko(self):
        tefal = Skovoroda()
        tefal.put('salo')
        tefal.put('bolshesala')
        tefal.put('maslo')
        tefal.put('salo')
        tefal.put('hleb')
        self.assertRaises(SkovorodaOverflowException, tefal.put('vodka'))


class TestZarkiKotletki(unittest.TestCase):
    def test_is_kotletka_up(self):
        kotletka = Kotletka()
        kotletka.turn_over()
        self.assertFalse(kotletka.up)

    def test_how_many_time_turned_over(self):
        kotletka = Kotletka()
        kotletka.turn_over()
        kotletka.turn_over()
        self.assertEqual(kotletka._times_turned, 2)

    def test_is_kotletka_ready(self):
        kotletka = Kotletka()
        for _ in itertools.repeat(None, kotletka.recommended_turns):
            kotletka.turn_over()
        self.assertTrue(kotletka.ready)


class TestSlozeniaBurgera(unittest.TestCase):
    def test_make_burger(self):
        kotletka = Kotletka()
        tefal = Skovoroda()
        tefal.put(kotletka)
        for _ in itertools.repeat(None, Kotletka.recommended_turns):
            kotletka.turn_over()

        top_bun = Bun()
        bottom_bun = Bun()
        sauce = Sauce()
        cathcupketchup = Ketchup()

        burger = Burger(
          kotletka,
          [top_bun, bottom_bun],
          cathcupketchup)

    def test_throw_burger_exception(self):
        kotletka = Kotletka()
        top_bun = Bun()
        bottom_bun = Bun()
        sauce = Sauce()
        cathcupketchup = Ketchup()

        with self.assertRaises(YouSuckAtCookingException):
            burger = Burger(
              kotletka,
              [top_bun, bottom_bun],
              cathcupketchup)


if __name__ == '__main__':
    unittest.main()
