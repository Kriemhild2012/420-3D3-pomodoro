import tkinter as tk
from observers.observer import Observateur


class AffichageEtat(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="Travail", font=("Arial", 16, "bold"))
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez etat depuis sujet.get_donnees()
        # Mettez à jour le label
        # Couleur : noir pour "Travail", bleu pour "Pause"
        etat = sujet.get_donnees()["etat"]
        self._label.config(text=etat, fg="black" if etat == "Travail" else "blue")
        