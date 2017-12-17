import unittest
from test1 import emulate
from prosynt import findEntryAndSize

class TestProsynt(unittest.TestCase):

  def test_emulate(self):
    r_ecx, r_edx = emulate()
    self.assertEqual(r_ecx, 0x1235)
    self.assertEqual(r_edx, 0x788f)

  def test_findEntryAndSize(self):
    ep, sz = findEntryAndSize("./test_resources/xor")
    self.assertEqual(ep, 1088)
    self.assertEqual(sz, 514)

if __name__ == '__main__':
  unittest.main()
