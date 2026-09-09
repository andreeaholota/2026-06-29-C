import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handleCreaGrafo(self, e):

        self._model.creaGrafo()

        nodi = self._model.getNumberNodes()
        archi = self._model.getNumberEdges()

        self._view.txt_result.controls.clear()

        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi = {nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi = {archi}"))

        self._view.update_page()

    def handleStampaInfo(self,e):
        try:
            artista_grado, grado = self._model.getGradoMassimo()
            artista_peso, peso = self._model.getSommaPesiMax()
            top_archi = self._model.getSortedEdges()
        except Exception as ex:
            self._view.create_alert(f"Errore nella stampa delle informazioni: {ex}")
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Artista con grado maggiore: {artista_grado.name} (grado {grado})"))
        self._view.txt_result.controls.append(
            ft.Text(f"Artista con somma pesi massima: {artista_peso.name} (somma {peso})"))
        self._view.txt_result.controls.append(ft.Text("Top 10 archi per peso:"))
        for a1, a2, dati in top_archi:
            self._view.txt_result.controls.append(ft.Text(f"  {a1.name} - {a2.name}: peso {dati['weight']}"))

        self._view.update_page()

    def handleSelezione(self,e):
        pass