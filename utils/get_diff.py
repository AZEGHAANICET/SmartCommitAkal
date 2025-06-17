import subprocess

def get_diff():
    """
    Récupère les différences (diff) des fichiers mis en scène (staged) dans le dépôt Git local.

    Cette fonction exécute la commande `git diff --cached` pour obtenir les modifications
    qui ont été ajoutées à l'index (prêtes à être commit) mais qui ne sont pas encore commitées.
    Le résultat est retourné sous forme de chaîne de caractères.

    Returns:
        str: La sortie textuelle de la commande `git diff --cached`, c’est-à-dire les différences
             entre la version indexée et la dernière version commitée. Si aucune différence
             n’est détectée ou en cas d’erreur, retourne une chaîne vide.

    Raises:
        subprocess.CalledProcessError: Si la commande git retourne un code d’erreur différent de 0,
                                      cette exception peut être levée (capturée dans la fonction et
                                      gérée en renvoyant une chaîne vide).

    Exemple:
        >>> diff = get_diff()
        >>> if diff:
        ...     print("Différences détectées :")
        ...     print(diff)
        ... else:
        ...     print("Aucune différence détectée ou erreur.")
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--cached"],
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )
        print(result.stdout)
        return result.stdout
    except Exception:
        return ""
