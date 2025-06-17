"""
SmartCommit - Générateur simple de messages de commit
"""

import subprocess
import sys
import os
from openai import OpenAI
from utils.generate_message import generate_message
from utils.get_diff import get_diff


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <fichier_message>")
        sys.exit(1)

    diff = get_diff()
    if not diff.strip():
        print("Aucune modification détectée.")
        sys.exit(0)

    message = generate_message(diff)
    with open(sys.argv[1], "w") as f:
        f.write(message + "\n")

    print(f"Message généré : {message}")

if __name__ == "__main__":
    main()
