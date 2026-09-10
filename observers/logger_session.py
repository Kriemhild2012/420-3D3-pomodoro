from datetime import datetime
from observers.observer import Observateur


class LoggerSession(Observateur):

    def __init__(self, chemin_fichier: str = "pomodoro.log"):
        self._chemin = chemin_fichier
        self._derniere_session = 0

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez sessions_completees depuis sujet.get_donnees()
        # Écrivez dans le fichier SEULEMENT si une nouvelle session est complétée
        # (comparez avec self._derniere_session)
        # Mettez à jour self._derniere_session
        pass
