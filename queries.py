from conexaoDB import *
def ler_todos_usuarios(bd):
    return ler_bd(bd, "SELECT * FROM Usuario")
def ler_usuario_nome(bd, nome):
    query = "SELECT * FROM Usuario WHERE nome LIKE ?"
    return ler_bd(bd, query, ('%'+nome+'%',))
