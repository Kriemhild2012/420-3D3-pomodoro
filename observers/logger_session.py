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
        sessions_completees = sujet.get_donnees()["sessions_completees"]
        if sessions_completees > self._derniere_session:
            with open(self._chemin, "a") as f:
                f.write(f"Session complétée à {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            self._derniere_session = sessions_completees
        else:
            return  # Ne rien faire si aucune nouvelle session n'est complétée
