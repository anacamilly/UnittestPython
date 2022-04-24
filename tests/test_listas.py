from listas import *
import unittest
class TestOrdenacaoListas(unittest.TestCase):
 def test_valores_entrada(self):
    self.assertRaises(TypeError, ordenar_lista, ['um', 0, 10])
    self.assertRaises(TypeError, ordenar_lista, [20.5, 1, True])
 def test_ordenacao(self):
    self.assertEqual(ordenar_lista([4, 5, 3, 2.2, 4.1]), [2.2, 3, 4, 4.1, 5])
    self.assertEqual(ordenar_lista([4, 0, 0, 2.2, 4.1]), [0, 0, 2.2, 4, 4.1])
    self.assertEqual(ordenar_lista([4, 4, -2, -2.2, 4.1]), [-2.2, -2, 4, 4, 4.1])
