# Projet A — Minuteur Pomodoro

Application de minuteur Pomodoro avec interface graphique tkinter.

## Lancement

```bash
python app.py
```

## Travail à faire avant le cours

1. Forkez ce dépôt dans votre compte GitHub
2. Lisez attentivement le code de la branche `main`
3. Examinez la branche `refactor` - elle contient un squelette à compléter
4. Posez-vous les questions suivantes :
   - Que fait la méthode `tick()` exactement ?
   - Quels seraient les observateurs naturels de cette application ?
   - Comparez la structure de `app.py` avec la structure de la branche `refactor`

## Structure de la branche `refactor`

```
pomodoro/
├── main.py
├── models/
│   ├── subject.py      ← interface Sujet (complète)
│   └── minuteur.py     ← sujet concret (à compléter)
├── observers/
│   ├── observer.py     ← interface Observateur (complète)
│   ├── affichage_temps.py    ← à compléter
│   ├── affichage_etat.py     ← à compléter
│   ├── barre_progression.py  ← à compléter
│   ├── compteur_sessions.py  ← à compléter
│   └── logger_session.py     ← à compléter
└── views/
    └── dashboard.py    ← à compléter
```
