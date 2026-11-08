from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""



class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        connessione = DBConnect.get_connection()
        if connessione is None:
            return []
        cursore = connessione.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro"
        cursore.execute(query)
        righe = cursore.fetchall()

        lista_generi = []
        for riga in righe:
            lista_generi.append(riga["genere"])
        cursore.close()
        connessione.close()

        return lista_generi

    def get_libri_filtrati(self, biblioteca, genere):
        connessione = DBConnect.get_connection()
        if connessione is None:
            return []

        cursore = connessione.cursor(dictionary=True)
        query = "SELECT * FROM libro WHERE biblioteca = %s AND genere = %s"
        cursore.execute(query, (biblioteca, genere))
        righe = cursore.fetchall()

        lista_libri = []
        for riga in righe:
            nuovo_libro = Libro(**riga)
            lista_libri.append(nuovo_libro)

        cursore.close()
        connessione.close()

        return lista_libri
