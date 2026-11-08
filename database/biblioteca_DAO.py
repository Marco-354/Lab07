from database.DB_connect import DBConnect

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass
    def get_biblioteche(self):
        connessione = DBConnect.get_connection()
        if connessione is None:
            return []
        cursore = connessione.cursor(dictionary=True)
        query = "SELECT nome FROM biblioteca"
        cursore.execute(query)
        righe = cursore.fetchall()
        lista_biblioteche = []
        for riga in righe:
            lista_biblioteche.append(riga["nome"])
        cursore.close()
        connessione.close()

        return lista_biblioteche

