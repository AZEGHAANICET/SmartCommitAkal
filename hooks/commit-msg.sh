#!/bin/sh
COMMIT_FILE="$1"

if command -v python &> /dev/null; then
    PYTHON=python
else command -v python3 &> /dev/null; then
    PYTHON=python3
fi

if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ La variable d'environnement OPENAI_API_KEY n'est pas définie."
    echo "Définissez-la avant de continuer."
    exit 1
fi

SMARTCOMMIT_SCRIPT="./smartcommitakal/main.py"

if [ ! -f "$SMARTCOMMIT_SCRIPT" ]; then
    echo "❌ Script SmartCommit non trouvé : $SMARTCOMMIT_SCRIPT"
    echo "feat: mise à jour du code" > "$COMMIT_FILE"
    exit 0
fi

echo "🤖 SmartCommit génère votre message de commit..."

$PYTHON "$SMARTCOMMIT_SCRIPT" "$COMMIT_FILE"
RESULT=$?

if [ $RESULT -eq 0 ]; then
    echo "✅ Message de commit généré avec succès !"
else
    echo "⚠️ Erreur lors de la génération du message de commit."
    echo "feat: mise à jour du code" > "$COMMIT_FILE"
fi

exit $RESULT
