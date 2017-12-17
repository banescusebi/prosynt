import unittest
from test1 import emulate

class TestProsynt(unittest.TestCase):

  def test_emulate(self):
    r_ecx, r_edx = emulate()
    self.assertEqual(r_ecx, 0x1235)
    self.assertEqual(r_edx, 0x788f)

if __name__ == '__main__':
  unittest.main()
