from volume_cubo import *
import unittest
class TestCubo(unittest.TestCase):
 def test_volume(self):
    self.assertAlmostEqual(calculo_volume_cubo(2),8)
    self.assertAlmostEqual(calculo_volume_cubo(1),1)
    self.assertAlmostEqual(calculo_volume_cubo(5.5),166.375)
 def test_valores_entrada(self):
    self.assertRaises(TypeError, calculo_volume_cubo, True)
 def test_valores_permitidos(self):
    self.assertRaises(ValueError, calculo_volume_cubo, -5)
    self.assertRaises(ValueError, calculo_volume_cubo, 0)
