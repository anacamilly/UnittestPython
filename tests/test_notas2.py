from notas2 import *
import unittest
class TestDashboard(unittest.TestCase):
 def test_arredondamento(self):
    self.assertEqual(percentual_arredondado(5, 13), 0.3846)
    self.assertEqual(percentual_arredondado(5, 10), 0.5000)
    self.assertEqual(percentual_arredondado(1, 6), 0.1667)
 def test_percentual_status(self):
    situacao1 = [('Carla', 7.8, False, False), ('Danilo', 7.8, True, False), ('Daniel', 5.4, False, True),
    ('Alice', 8.5, False, True), ('Flávio', 8.4, False, True), ('Silvia', 2.4, False, True)]
    self.assertEqual(percentual_status(situacao1), (0.1667, 0.5, 0.1667, 0.1667))
