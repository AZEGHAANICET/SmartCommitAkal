# SmartCommit 🤖

Générateur automatique de messages de commit avec l'IA.


## Configuration

Définissez votre clé API OpenAI :
Tout d'abord installer l'application Git bash
Ensuite taper la commande suivante :

```bash
set OPENAI_API_KEY="votre-clé-api"
```

## Structure

```
SmartCommitAkal/
├── main.py                    # Script principal
├── hooks/
│   └── commit-msg  # Hook Git
└── requirements.txt           # Dépendances
```

## Utilisation

1. `git add .` - Ajouter vos fichiers
2. `git commit -m "a"` - SmartCommit génère le message automatiquement
