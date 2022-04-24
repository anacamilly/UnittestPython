from listas2 import *
import unittest

class TestMenorElementoLista(unittest.TestCase):
   def test_valores_entrada(self):
      self.assertRaises(TypeError, menor_elemento_lista, ['um', 0, 10])
      self.assertRaises(TypeError, menor_elemento_lista, [20.5, 1, True])
   def test_menor_elemento(self):
      self.assertEqual(menor_elemento_lista([4, 5, 3, 2.2, 4.1]), (2.2, 3))
      self.assertEqual(menor_elemento_lista([4, 0, 0, 2.2, 4.1]), (0, 1))
      self.assertEqual(menor_elemento_lista([4, 4, -2, -2.2, 4.1]), (-2.2, 3))
      self.assertEqual(menor_elemento_lista([-20, 4, -2, -2.2, 4.1]), (-20, 0))
