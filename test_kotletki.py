import itertools
import unittest
from kotletki import Kotletka, Bun, Sauce, Ketchup, Skovoroda
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
        for _ in itertools.repeat(None, 5):
            kotletka.turn_over()
        self.assertTrue(kotletka.ready)


class TestSlozeniaBurgera(unittest.TestCase):
    def test_is_burger_ready(self):
        kotletka = Kotletka()
        bun = Bun()
        sauce = Sauce()
        cathcupketchup = Ketchup()
        tefal = Skovoroda()
        for _ in itertools.repeat(None, 5):
            kotletka.turn_over()
        tefal.put(kotletka)
        tefal.put(bun)
        tefal.put(sauce)
        tefal.put(cathcupketchup)
        self.assertTrue(kotletka.ready)

    def test_throw_burger_exception(self):
        kotletka = Kotletka()
        bun = Bun()
        sauce = Sauce()
        cathcupketchup = Ketchup()
        tefal = Skovoroda()
        tefal.put(bun)
        tefal.put(sauce)
        tefal.put(cathcupketchup)
        self.assertRaises(YouSuckAtCookingException, tefal.put(kotletka))


if __name__ == '__main__':
    unittest.main()
