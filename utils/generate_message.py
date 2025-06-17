from openai import OpenAI
import os
from prompts import PROMPT
def generate_message(diff):
    """
    Génère un message de commit Git pertinent à partir d'une différence (diff) de code en utilisant l'API OpenAI.

    Cette fonction utilise le modèle GPT-3.5-turbo d'OpenAI pour analyser la différence de code fournie 
    et générer automatiquement un message de commit clair et concis. En cas d'erreur (ex: clé API manquante ou 
    problème réseau), un message par défaut est retourné.

    Args:
        diff (str): Chaîne de caractères représentant la différence (diff) de code à analyser.

    Returns:
        str: Un message de commit généré automatiquement décrivant les modifications, 
             ou un message par défaut "feat: mise à jour du code" en cas d'erreur ou de contenu vide.

    Exemple d'utilisation:
        >>> diff = "diff --git a/app.py b/app.py\nindex e69de29..b6fc4c6 100644\n--- a/app.py\n+++ b/app.py\n@@ -0,0 +1,2 @@\n+print('Hello world')"
        >>> message = generate_message(diff)
        >>> print(message)
        "feat: ajout d'un affichage 'Hello world' dans app.py"

    Remarques:
        - La variable d'environnement "OPENAI_API_KEY" doit être définie avant d'appeler cette fonction.
        - La variable globale PROMPT doit être définie et contenir une chaîne avec un placeholder '{diff}' pour injecter la différence.
        - La fonction utilise un appel API avec un maximum de 100 tokens et une température de 0.7 pour un message créatif mais contrôlé.
    """
    try:
        api_key = os.environ["OPENAI_API_KEY"]
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": PROMPT.format(diff=diff)}],
            max_tokens=100,
            temperature=0.7
        )

        content = response.choices[0].message.content.strip()
        return content.strip() if content else "feat: mise à jour du code"
    except Exception:
        return "feat: mise à jour du code"
