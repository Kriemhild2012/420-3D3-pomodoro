import tkinter as tk
from observers.observer import Observateur


class AffichageTemps(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="25:00", font=("Arial", 48, "bold"))
        self._label.pack(pady=10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant depuis sujet.get_donnees()
        # Calculez minutes et secondes
        # Mettez à jour le label au format "MM:SS"
        pass
