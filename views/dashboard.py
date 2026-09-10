import tkinter as tk
from models.minuteur import Minuteur
from observers.affichage_temps import AffichageTemps
from observers.affichage_etat import AffichageEtat
from observers.barre_progression import BarreProgression
from observers.compteur_sessions import CompteurSessions
from observers.logger_session import LoggerSession


class Dashboard(tk.Tk):

    INTERVALLE_MS = 1000

    def __init__(self, minuteur: Minuteur):
        super().__init__()
        self.title("Minuteur Pomodoro")
        self.resizable(False, False)
        self._minuteur = minuteur
        self._en_marche = False

        self._creer_observateurs()
        self._abonner_observateurs()
        self._creer_boutons()

    def _creer_observateurs(self) -> None:
        # À compléter :
        # Instanciez AffichageEtat, AffichageTemps, BarreProgression,
        # CompteurSessions et LoggerSession
        pass

    def _abonner_observateurs(self) -> None:
        # À compléter :
        # Abonnez tous les observateurs au minuteur
        pass

    def _creer_boutons(self) -> None:
        frame = tk.Frame(self)
        frame.pack(pady=10)

        self._btn_start = tk.Button(frame, text="Démarrer", command=self._demarrer)
        self._btn_start.pack(side=tk.LEFT, padx=5)

        self._btn_pause = tk.Button(
            frame, text="Pause", command=self._pause, state=tk.DISABLED
        )
        self._btn_pause.pack(side=tk.LEFT, padx=5)

        self._btn_reset = tk.Button(frame, text="Réinitialiser", command=self._reset)
        self._btn_reset.pack(side=tk.LEFT, padx=5)

    def _demarrer(self) -> None:
        # À compléter :
        # Activez le minuteur et démarrez la boucle _tick()
        # Mettez à jour les boutons
        pass

    def _pause(self) -> None:
        # À compléter :
        # Appelez basculer_pause() sur le minuteur
        # Mettez à jour le texte du bouton
        # Si on reprend, relancez _tick()
        pass

    def _reset(self) -> None:
        # À compléter :
        # Réinitialisez le minuteur
        # Mettez à jour les boutons
        pass

    def _tick(self) -> None:
        # À compléter :
        # Si en marche et pas en pause : appeler minuteur.tick()
        # Planifier le prochain appel avec self.after()
        pass
