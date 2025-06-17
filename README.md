# SmartCommit 🤖

**Générateur automatique de messages de commit avec l’IA.**

---

## Configuration

1. Installez Git Bash (pour Windows) si ce n’est pas déjà fait.

2. Définissez votre clé API OpenAI dans votre terminal avec la commande suivante :

```bash
# Windows (Git Bash)
export OPENAI_API_KEY="votre-clé-api"

# Linux/macOS
export OPENAI_API_KEY="votre-clé-api"

```
SmartCommitAkal/
├── main.py                    # Script principal générant le message de commit
├── hooks/
│   └── commit-msg             # Hook Git pour générer automatiquement le message de commit
└── requirements.txt           # Liste des dépendances Python
```
