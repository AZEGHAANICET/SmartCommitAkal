
# SmartCommit 🤖

Générateur automatique de messages de commit avec l’IA.

---

## Présentation

SmartCommit utilise OpenAI pour générer automatiquement un message clair et concis à partir des modifications en staging dans votre dépôt Git. Ce script Python s’intègre facilement à votre workflow Git grâce à un hook `commit-msg`.

---

## Prérequis

- Python 3.7 ou supérieur installé
- Git installé
- Clé API OpenAI (à obtenir sur https://platform.openai.com/account/api-keys)
- Git Bash (pour Windows)

---

## Installation & Configuration

1. **Cloner le dépôt SmartCommitAkal** (ou placer les fichiers dans un dossier) :

```bash
git clone <votre-depot-smartcommit>
cd SmartCommitAkal
```

2. **Installer les dépendances Python :**

```bash
pip install -r requirements.txt
```

3. **Définir la variable d’environnement OPENAI_API_KEY dans votre terminal :**

- Sous Linux/macOS ou Git Bash (Windows) :

```bash
export OPENAI_API_KEY="votre-clé-api"
```


4. **Installer le hook Git pour le commit automatique du message :**

Copiez le fichier `commit-msg` dans le dossier `.git/hooks/` de votre projet Git :

```bash
cp hooks/commit-msg .git/hooks/
chmod +x .git/hooks/commit-msg
```

---

## Structure du projet

```
SmartCommitAkal/
├── main.py                    # Script principal générant le message de commit
├── hooks/
│   └── commit-msg             # Hook Git pour générer automatiquement le message de commit
└── requirements.txt           # Liste des dépendances Python
```

---

## Utilisation

1. Ajouter vos fichiers au staging :

```bash
git add .
```

2. Lancer la commande de commit classique (avec un message temporaire, car impossible de lancer sans dans les configs internes de git) :

```bash
git commit -m "a"
```

Le hook `commit-msg` interceptera la commande, analysera les changements et remplacera le message de commit par un message généré automatiquement via OpenAI.

---

## Fonctionnement

- Le script récupère le diff des fichiers en staging (`git diff --cached`)
- Il envoie ce diff à l’API OpenAI GPT-3.5-turbo via un prompt prédéfini.
- Il récupère un message de commit formaté (type: description).
- Le hook remplace le message de commit par ce message généré.

---

## Remarques

- Si aucun changement n’est détecté, le commit sera annulé.
- Si l’API OpenAI ne répond pas ou qu’une erreur survient, un message par défaut est utilisé : `feat: mise à jour du code`.
- Le script est prévu pour être simple et facilement modifiable.

---

## Exemple de commande

```bash
git add .
git commit -m "a"
```

---

## Contact
Pour toute question ou contribution, contactez-moi ou ouvrez une issue sur le dépôt.
📧 loicanicetazegha@gmail.com
*Bonne utilisation de SmartCommit !*