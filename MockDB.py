from unittest import TestCase
import sys
sys.path.insert(0, '..')
from conexaoDB import *
BD = "TestBD.db"
class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()
        query_criar_tabela_usuario = """CREATE TABLE Usuario (id int NOT NULL PRIMARY KEY , nome text NOT NULL, email text NOT NULL)"""
        query_criar_tabela_turma = """CREATE TABLE Turma (id int NOT NULL PRIMARY KEY , numero int NOT NULL)"""
        query_criar_tabela_disciplina = """CREATE TABLE Disciplina (id int NOT NULL PRIMARY KEY , nome text NOT NULL)"""
        try:
            cursor.execute(query_criar_tabela_usuario)
            cursor.execute(query_criar_tabela_turma)
            cursor.execute(query_criar_tabela_disciplina)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")
            query_inserir_usuario = """INSERT INTO Usuario (id, nome, email) VALUES
            (1, 'Carla F.', 'c@c.com'),
            (2, 'Danilo', 'd@d.com'),
            (3, 'Daniel', 'd2@d2.com'),
            (4, 'Alice', 'a@a.com')"""
            query_inserir_turma = """INSERT INTO Turma (id, numero) VALUES
            (1, 23),
            (2, 2),
            (3, 8),
            (4, 10)"""
            query_criar_tabela_disciplina = """CREATE TABLE Disciplina (
            id int NOT NULL PRIMARY KEY ,
            nome text NOT NULL)"""
            try:
                cursor.execute(query_criar_tabela_usuario)
                cursor.execute(query_criar_tabela_turma)
                cursor.execute(query_criar_tabela_disciplina)
                con.commit()
            except sqlite3.Error as error:
                print("Erro na criação das tabelas:", error)
            else:
                    print("Criação das tabelas: OK")
                    query_inserir_usuario = """INSERT INTO Usuario (id, nome, email) VALUES
                    (1, 'Carla F.', 'c@c.com'),
                    (2, 'Danilo', 'd@d.com'),
                    (3, 'Daniel', 'd2@d2.com'),
                    (4, 'Alice', 'a@a.com')"""
                    query_inserir_turma = """INSERT INTO Turma (id, numero) VALUES
                    (1, 23),
                    (2, 2),
                    (3, 8),
                    (4, 10)"""
    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()
        try:
            cursor.execute("DROP TABLE Usuario")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Disciplina")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)
