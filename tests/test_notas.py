from notas import *
import unittest
class TestTerceiraProva(unittest.TestCase):
 def test_nota_necessaria(self):
    notas_aluno1 = [3, 5.6, 0]
    notas_aluno2 = [3, 0, 0]
    notas_aluno3 = [10, 10, 0]
    self.assertEqual(nota_necessaria(notas_aluno1),12.4)
    self.assertEqual(nota_necessaria(notas_aluno2),18)
    self.assertEqual(nota_necessaria(notas_aluno3),1)
