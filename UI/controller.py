import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    #TODOO
    def popola_dropdowns(self):
        # 1. Svuoto prima le opzioni
        self._view.dd_biblioteca.options.clear()
        self._view.dd_genere.options.clear()

        # 2. Recupero i dati dal model
        # (se il tuo model ha nomi diversi, cambiali qui!)
        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()

        # 3. Riempio il dropdown delle biblioteche
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b))

        # 4. Riempio il dropdown dei generi
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(g))

        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def handle_select_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value
        print(f"Biblioteca scelta: {self.biblioteca_selezionata}")

    def handle_select_genere(self, e):
        self.genere_selezionato = self._view.dd_genere.value
        print(f"Genere scelto: {self.genere_selezionato}")

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_mostra_libri(self, e):
        # Se non si seleziona ninete lancio errore
        if self.biblioteca_selezionata is None or self.genere_selezionato is None:
            self._view.show_alert("Seleziona sia una biblioteca che un genere prima di cercare!")
            return

        # Svuoto i risultati precedenti
        self._view.lv_libri.controls.clear()
        libri = self._model.get_libri(self.biblioteca_selezionata, self.genere_selezionato)

        # Se non trovo niente avviso l'utente
        if len(libri) == 0:
            self._view.lv_libri.controls.append(ft.Text("Nessun libro trovato per questa ricerca."))
        else:
            # Altrimenti li stampo tutti
            for libro in libri:
                self._view.lv_libri.controls.append(ft.Text(f"📚 {libro}"))

        self._view.update()
