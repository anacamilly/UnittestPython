from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries import *
class TestDB(MockBD):
    def test_select_all(self):
        retorno_esperado = [(1, 'Carla F.', 'c@c.com'),
                            (2, 'Danilo', 'd@d.com'),
                            (3, 'Daniel', 'd2@d2.com'),
                            (4, 'Alice', 'a@a.com')]
        self.assertEqual(ler_todos_usuarios(self.mock_db_config.get('bd')), 
        retorno_esperado)
    def test_filtro_nome(self):
        retorno_esperado = [(1, 'Carla F.', 'c@c.com')]
        self.assertEqual(ler_usuario_nome(self.mock_db_config.get('bd'), 'Carla'),  
        retorno_esperado)
