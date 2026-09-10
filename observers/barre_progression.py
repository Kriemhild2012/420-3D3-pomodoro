import tkinter as tk
from observers.observer import Observateur


class BarreProgression(Observateur):

    def __init__(self, parent):
        self._canvas = tk.Canvas(parent, width=300, height=20, bg="white")
        self._canvas.pack(pady=10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant et duree_totale depuis sujet.get_donnees()
        # Calculez la largeur proportionnelle (300 * temps_restant / duree_totale)
        # Effacez le canvas et dessinez le rectangle
        pass
