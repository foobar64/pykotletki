import unittest
import itertools
from kotletki import Kotletka

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

if __name__ == '__main__':
    unittest.main()
