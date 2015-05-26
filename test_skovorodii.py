import unittest
from kotletki import Skovoroda
from kotletki import SkovorodaOverflowException

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

unittest.main()
